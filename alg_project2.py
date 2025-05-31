import matplotlib.pyplot as plt
import networkx as nx

def input_graph():
    """Take undirected graph input"""
    graph = {}
    print("Enter edges (vertex1 vertex2 weight). Type 'done' when finished.")
    
    while True:
        edge_input = input("Edge (or 'done'): ").strip()
        if edge_input.lower() == 'done':
            break

        u, v, w = edge_input.split()
        w = int(w)

        # Add edges both ways (undirected)
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph

def kruskal(graph):
    # Collect all unique edges
    edges = []
    for u in graph:
        for v, weight in graph[u]:
            edge = (weight, min(u, v), max(u, v))
            if edge not in edges:
                edges.append(edge)

    edges.sort()  # Sort edges by weight
    vertices = list(graph.keys())
    n = len(vertices)
    
    # Initialize Union-Find data structure
    parent = list(range(n))
    rank = [0] * n
    
    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])   # Go up until the root, and flatten the path.
        return parent[i]

    # Connecting two trees(components)
    def merge(p, q):
        if rank[p] < rank[q]:
            parent[p] = q
        else:
            parent[q] = p
            if rank[p] == rank[q]:
                rank[p] += 1

    # Find MST
    mst_edges = []
    count = 0
    i = 0
    
    while count < n - 1:
        weight, u, v = edges[i]
        i += 1
        u_idx = vertices.index(u)
        v_idx = vertices.index(v)
        p = find(u_idx)
        q = find(v_idx)
        
        if p != q:
            merge(p, q)
            mst_edges.append((u, v, weight))
            count += 1

    return mst_edges, sum(w for _, _, w in mst_edges)

def draw_mst(graph, mst_edges): 
    """Draw the MST using matplotlib and networkx"""

    G = nx.Graph()

    # Add all vertices
    for vertex in graph:
        G.add_node(vertex)

    # Add only MST edges
    for u, v, weight in mst_edges:
        G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G)
    edge_labels = {(u, v): f'{w}' for u, v, w in mst_edges}
    nx.draw(G, pos, with_labels=True, node_color='red', node_size=500, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Minimum Spanning Tree (Kruskal's Algorithm)")
    plt.show()

def main():
    print("Kruskal's Algorithm - Minimum Spanning Tree")
    graph = input_graph()
    
    if not graph:
        print("No graph input received.")
        return

    mst_edges, total_weight = kruskal(graph)

    print("\nMinimum Spanning Tree Edges:")
    for u, v, weight in mst_edges:
        print(f"{u} -- {v} (weight: {weight})")
    print(f"Total weight of MST: {total_weight}")

    draw_mst(graph, mst_edges)

if __name__ == "__main__":
    main()
