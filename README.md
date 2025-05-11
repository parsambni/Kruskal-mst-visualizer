# Kruskal's Algorithm - Minimum Spanning Tree (MST) Visualizer

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![NetworkX](https://img.shields.io/badge/NetworkX-2.5+-orange.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.3+-green.svg)

A Python implementation of Kruskal's algorithm for finding the Minimum Spanning Tree (MST) of an undirected weighted graph, with visualization capabilities.

## Features

- Interactive graph input from the command line
- Implementation of Kruskal's algorithm with Union-Find (Disjoint Set Union) data structure
- Visualization of the resulting MST using NetworkX and Matplotlib
- Displays edge weights and total MST weight
- Handles duplicate edges automatically

## Requirements

- Python 3.6+
- NetworkX (`pip install networkx`)
- Matplotlib (`pip install matplotlib`)

## How to Use

1. Clone the repository or download the Python file
2. Run the script: `python alg_project2.py`
3. Enter edges in the format: `vertex1 vertex2 weight`
4. Type `done` when finished entering edges
5. View the MST edges and total weight in the console
6. A visualization window will pop up showing the MST

### Example Input:
```
Enter edges in the format: vertex1 vertex2 weight
Type 'done' when finished.

Edge (or 'done'): A B 4
Edge (or 'done'): B C 8
Edge (or 'done'): C D 7
Edge (or 'done'): D E 9
Edge (or 'done'): E F 10
Edge (or 'done'): F G 2
Edge (or 'done'): G H 1
Edge (or 'done'): H A 8
Edge (or 'done'): B H 11
Edge (or 'done'): C I 2
Edge (or 'done'): I H 7
Edge (or 'done'): I G 6
Edge (or 'done'): C F 4
Edge (or 'done'): D F 14
Edge (or 'done'): done
```

## Output

The program will display:
- All edges in the MST with their weights
- Total weight of the MST
- A visual graph of the MST

## Implementation Details

- Uses Union-Find with path compression and union by rank for efficient component tracking
- Graph visualization uses NetworkX's spring layout
- Edge weights are displayed on the visualized graph

## License

This project is open source and available under the MIT License.
