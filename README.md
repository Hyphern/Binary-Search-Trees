# Binary Search Trees

A comprehensive Python implementation of binary search tree data structures, including standard BSTs, self-balancing AVL trees, and min-heaps.

## Overview

This library provides multiple tree-based data structures for efficient data storage and retrieval:

| Data Structure | File | Description |
|----------------|------|-------------|
| **Binary Search Tree** | `BinarySearchTree.py` | Standard BST with insert, search, delete operations |
| **AVL Tree** | `AVLTree.py` | Self-balancing BST that maintains O(log n) height |
| **Min Heap** | `Heap.py` | Priority queue implementation with O(log n) insert/extract |

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Binary-Search-Trees.git
cd Binary-Search-Trees

# Install test dependencies (optional)
pip install -r tests/requirements.txt
```

## Quick Start

```python
from BinarySearchTree import BinarySearchTree
from AVLTree import AVLTree
from Heap import MinHeap

# Binary Search Tree
bst = BinarySearchTree()
bst.insert(10, "ten")
bst.insert(5, "five")
bst.insert(15, "fifteen")
print(bst.get_value(10))  # Output: ten
bst.delete(10)

# AVL Tree (self-balancing)
avl = AVLTree()
for i in [10, 5, 15, 3, 7]:
    avl.insert(i, str(i))
print(avl.height)  # Output: 3 (balanced)

# Min Heap
heap = MinHeap()
heap.insert(5)
heap.insert(3)
heap.insert(7)
print(heap.extract().key)  # Output: 3 (minimum)
```

## Features

### Binary Search Tree (`BinarySearchTree.py`)

- **Insert**: O(h) time complexity where h is tree height
- **Search**: O(h) lookup by key
- **Delete**: O(h) with inorder successor replacement
- Supports key-value pairs

### AVL Tree (`AVLTree.py`)

- Self-balancing using rotations (left/right)
- Maintains O(log n) height guarantee
- Height tracking for each node
- Balance factor monitoring
- All standard BST operations in O(log n)

### Min Heap (`Heap.py`)

- Linked binary heap implementation
- **Insert**: O(log n) using sift-up
- **Extract min**: O(log n) using sift-down
- **Delete by node**: O(log n)
- Index-based node access
- Full parent/child relationship tracking

### Range Query (`BST.py`)

```python
from BST import range_query

# Find all keys in range [low, high]
results = range_query(bst, low=5, high=20)
# Returns: [(5, "five"), (10, "ten"), (15, "fifteen"), ...]
```

## Time Complexities

| Operation | BST (average) | BST (worst) | AVL Tree | Min Heap |
|-----------|---------------|-------------|----------|----------|
| Insert    | O(log n)     | O(n)        | O(log n) | O(log n) |
| Search    | O(log n)     | O(n)        | O(log n) | N/A      |
| Delete    | O(log n)     | O(n)        | O(log n) | O(log n) |
| Extract   | N/A          | N/A         | N/A      | O(log n) |

## Project Structure

```
Binary-Search-Trees/
├── AVLTree.py           # Self-balancing AVL tree
├── BinarySearchTree.py # Standard binary search tree
├── BinaryTree.py       # Base binary tree class
├── BST.py              # Abstract BST base class + range_query
├── FunTree.py          # Functional tree implementation
├── Heap.py             # MinHeap implementation
├── MarketTracker.py    # Application example
├── PriceTracker.py     # Application example
├── TreeNode.py         # Tree node implementation
├── TreePrinter.py      # Tree visualization utility
├── Node.py             # Alternative node implementation
├── tests/              # Unit tests
└── .github/workflows/  # CI/CD pipelines
```

## Testing

```bash
# Run all tests
pytest tests/

# Run specific test files
pytest tests/test_lab_6.py
pytest tests/test_lab_7.py
pytest tests/test_lab_8.py
pytest tests/test_lab_9.py
```

## Use Cases

- **Binary Search Tree**: General-purpose sorted data storage, range queries
- **AVL Tree**: When guaranteed O(log n) performance is required
- **Min Heap**: Priority queues, scheduling algorithms, Dijkstra's algorithm

## Requirements

- Python 3.7+
- pytest (for testing)

## License

MIT License
