# Reflection – Practical 5 (Binary Search Tree and Graph Traversal)

## 1. Binary Search Tree

### What I Learned
- Understood the core concept of how Binary Search Trees (BSTs) store data in sorted order.  
- Learned that insertion goes left if the new value is smaller and right if it is larger.  
- Practiced writing traversal methods (inorder, preorder, and postorder) and observed how each produces different outputs.

### Challenges Faced
- Initially struggled with handling cases where the tree was empty.  
- Got confused while writing recursive traversal functions, especially identifying the correct base case.  
- Sometimes the output order didn’t match my expectations, which required careful tracing.

### How I Overcame Them
- Drew tree diagrams on paper to visualize node placement.  
- Stepped through the recursive calls manually to understand the function’s flow.  
- Simplified the implementation by writing helper functions that handled one task at a time.

---

## 2. Graph Data Structure and Traversal Algorithms

### What I Learned
- Learned that graphs can be represented using adjacency lists and adjacency matrices.  
- Practiced implementing Breadth-First Search (BFS) and Depth-First Search (DFS) traversal algorithms.  
- Understood how traversal strategy affects the order in which nodes are visited.

### Challenges Faced
- Faced difficulty preventing infinite loops in cyclic graphs.  
- Initially forgot to reset the visited list between separate traversals.  
- Implementing BFS with a queue was challenging at first due to unfamiliarity with queue operations in Python.

### How I Overcame Them
- Used a set to track visited nodes and avoid revisiting them.  
- Printed the traversal order step-by-step to verify correctness.  
- Reviewed stack and queue operations in Python to better understand how BFS and DFS differ.

---

## Overall Reflection
This practical provided hands-on experience with two major data structures — Binary Search Trees and Graphs.  
Implementing them from scratch deepened my understanding of recursion, data relationships, and efficient searching/traversal methods.

### Future Improvements
- I aim to implement self-balancing trees such as AVL and Red-Black trees to manage uneven tree growth.  
- I also plan to explore advanced graph algorithms like Dijkstra’s and Prim’s to strengthen my understanding of graph theory and pathfinding.
