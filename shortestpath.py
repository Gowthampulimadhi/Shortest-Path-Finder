import heapq
from collections import defaultdict

    """
    A representation of a weighted, directed graph using an adjacency list.
    The adjacency list maps a node to a list of (neighbor, weight) tuples.
    """
    def __init__(self):
        self.adj = defaultdict(list)
        self.nodes = set()

    def add_edge(self, source, destination, weight):
        """
        Adds a directed, weighted edge from source to destination.
        """
        if weight < 0:
            print(f"Warning: Edge from {source} to {destination} has a negative weight ({weight}).")
            
        self.adj[source].append((destination, weight))
        
        self.nodes.add(source)
        self.nodes.add(destination)

    def get_nodes(self):
        """Returns all nodes in the graph."""
        return self.nodes
    
    def get_neighbors(self, node):
        """Returns the neighbors (and weights) for a given node."""
        return self.adj.get(node, [])


def dijkstra(graph, start_node, target_node):
    """
    Computes the shortest path from start_node to all other nodes in the graph 
    using Dijkstra's algorithm.

    :param graph: The Graph object.
    :param start_node: The starting node for the path search.
    :param target_node: The target node to find the path to.
    :returns: A tuple (total_weight, shortest_path) or None if no path exists.
    """
    
    priority_queue = [(0, start_node)]
    
    distances = {node: float('inf') for node in graph.get_nodes()}
    distances[start_node] = 0
    
   
    predecessors = {node: None for node in graph.get_nodes()}
    
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        
        visited.add(current_node)

        if current_node == target_node:
            break

        for neighbor, weight in graph.get_neighbors(current_node):
            
            distance_through_current = current_distance + weight
            
            if distance_through_current < distances[neighbor]:
                distances[neighbor] = distance_through_current
                predecessors[neighbor] = current_node
                
                heapq.heappush(priority_queue, (distance_through_current, neighbor))

    
    final_distance = distances.get(target_node, float('inf'))
    if final_distance == float('inf'):
        return (None, f"Path from {start_node} to {target_node} not found (disconnected or unreachable).")

    path = []
    current = target_node
    while current is not None:
        path.append(current)
        current = predecessors[current]
    
    shortest_path = path[::-1]

    return (final_distance, shortest_path)


def run_tests():
    print("--- Running Dijkstra's Algorithm Test Cases ---\n")

    print("Test 1: Standard Connected Graph (A to F)")
    graph1 = Graph()
    graph1.add_edge('A', 'B', 1)
    graph1.add_edge('A', 'C', 4)
    graph1.add_edge('B', 'C', 2)
    graph1.add_edge('B', 'D', 5)
    graph1.add_edge('C', 'E', 1)
    graph1.add_edge('D', 'F', 3)
    graph1.add_edge('E', 'D', 1)
    graph1.add_edge('E', 'F', 4)

    weight1, path1 = dijkstra(graph1, 'A', 'F')
    print(f"  Result: Weight={weight1}, Path={path1}")
    print(f"  Expected: Weight=8, Path=['A', 'B', 'C', 'E', 'D', 'F']")
    print("-" * 30)

    print("Test 2: Disconnected Graph (A to Z)")
    graph2 = Graph()
    graph2.add_edge('A', 'B', 1)
    graph2.add_edge('B', 'C', 1)
    graph2.add_edge('X', 'Y', 1) # A separate component
    
    graph2.nodes.add('Z') 
    
    weight2, path2 = dijkstra(graph2, 'A', 'Z')
    print(f"  Result: {path2}")
    print(f"  Expected: Path not found message.")
    print("-" * 30)
    
    print("Test 3: Negative Edge Weight (Demonstrating Limitation)")
    graph3 = Graph()
    graph3.add_edge('S', 'A', 1)
    graph3.add_edge('S', 'C', 2)
    graph3.add_edge('A', 'B', -5) # The negative edge
    graph3.add_edge('C', 'B', 1)
    graph3.add_edge('A', 'D', 3)
    
    weight3, path3 = dijkstra(graph3, 'S', 'B')
    print(f"  Result: Weight={weight3}, Path={path3}")
    print(f"  INCORRECT! Dijkstra's yields 3 (S->C->B). True shortest path is -4 (S->A->B).")
    print(f"  This demonstrates the limitation of Dijkstra's algorithm.")
    print("-" * 30)


if __name__ == "__main__":
    run_tests()