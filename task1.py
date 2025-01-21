import networkx as nx
import matplotlib.pyplot as plt

def create_graph(weighted=False):
    G = nx.Graph()

    # Adding nodes (e.g., city transport network)
    G.add_nodes_from([
        ("A", {"name": "Station A"}),
        ("B", {"name": "Station B"}),
        ("C", {"name": "Station C"}),
        ("D", {"name": "Station D"}),
        ("E", {"name": "Station E"})
    ])

    if weighted:
        # Adding weighted edges (e.g., distances between stations)
        G.add_weighted_edges_from([
            ("A", "B", 5),
            ("A", "C", 10),
            ("B", "D", 3),
            ("C", "D", 2),
            ("D", "E", 4)
        ])
    else:
        # Adding edges (connections between stations)
        G.add_edges_from([
            ("A", "B"),
            ("A", "C"),
            ("B", "D"),
            ("C", "D"),
            ("D", "E")
        ])

    return G

def analyze_graph(G):
    # Analysis of main characteristics
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degrees = dict(G.degree())

    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print("Degrees of nodes:")
    for node, degree in degrees.items():
        print(f"Node {node}: {degree}")

def visualize_graph(G):
    # Graph visualization
    pos = nx.spring_layout(G)  # Node positioning
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Transport Network Graph")
    plt.show()

if __name__ == "__main__":
    G = create_graph()
    analyze_graph(G)
    visualize_graph(G)