import matplotlib.pyplot as plt
import networkx as nx

def input_graph(): 
    """Take undirected graph input without asking for reverse edges"""

    graph = {}
    print("Enter edges in the format: vertex1 vertex2 weight")
    print("Type 'done' when finished.\n")

    while True:
        edge_input = input("Edge (or 'done'): ").strip()
        if edge_input.lower() == 'done':
            break

        parts = edge_input.split()
        if len(parts) != 3:
            print("Invalid format. Use: vertex1 vertex2 weight")
            continue

        u, v, w = parts
        try:
            w = int(w)
        except ValueError:
            print("Weight must be a number.")
            continue

        # Add edges both ways (undirected)
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        # Avoid duplicate edge entry
        if (v, w) not in graph[u]:
            graph[u].append((v, w))
        if (u, w) not in graph[v]:
            graph[v].append((u, w))

    return graph

def kruskal(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u]:
            # Ensure undirected edge uniqueness
            edge = (weight, min(u, v), max(u, v))
            if edge not in edges:
                edges.append(edge)


    # Sort all edges from smallest to largest weight
    edges.sort()

    vertices = list(graph.keys())
    n = len(vertices)

    vertex_index = {}               
    for i in range(len(vertices)):  
        v = vertices[i]             # Get the vertex at that index
        vertex_index[v] = i         # Map the vertex name to its index

    parent = list(range(n))
    rank = [0] * n

    # Finding root of a vertex
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

    mst_edges = []
    count = 0
    i = 0

    while count < n - 1:
        weight, u, v = edges[i]
        i += 1
        u_idx = vertex_index[u]    # Convert First Vertex to a number (e.g., 0)
        v_idx = vertex_index[v]    # Convert Second Vertex to a number (e.g., 1)
        p = find(u_idx)            # Find the root of First Vertex's group
        q = find(v_idx)            # Find the root of Second Vertex's group
        if p != q:
            merge(p, q)
            mst_edges.append((u, v, weight))
            count += 1

    total_weight = sum(w for _, _, w in mst_edges)
    return mst_edges, total_weight

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
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
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
    print(f"Total weight of MST: {total_weight}\n")

    draw_mst(graph, mst_edges)

if __name__ == "__main__":
    main()
