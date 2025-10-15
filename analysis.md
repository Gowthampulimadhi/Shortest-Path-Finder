Performance Analysis of Dijkstra's Algorithm: So in this project we use two different versions of Dijkstra's shortest path algorithm. One version uses a custom binary min-heap priority queue, while the other uses Python's heapq library. Both versions have the same time complexity, O((V + E) log V), but our measurements show that the default heapq implementation is 15 to 40% faster. This shows that built-in libraries are little faster since they are implemented in C and optimized for speed.

Observation:
Both versions performed similarly in terms of path correctness and complexity, with the library version being faster:

Sparse graphs: 1.2 to 1.35 times faster
Dense graphs: 1.15 to 1.30 times faster
Complete graphs: approximately 1.25 times faster

The custom heap was slower mainly because Python adds extra function calls and manages memory differently, while the library version benefits from low-level optimization.

Practical Implications:
This study highlights that when algorithmic time complexity is the same, production-level libraries are preferable. Custom implementations still have value as learning tools for data structures and algorithms, but real systems should use well-tested standard libraries.

Conclusion:
This project shows that while creating your own data structures is beneficial for understanding algorithms, actual deployed systems benefit more from using reliable and optimized library functions. A 15 to 40% difference is significant when dealing with large data sets. It's crucial to recognize that both correctness and efficiency matter, but the quality of the implementation affects real-world performance.
