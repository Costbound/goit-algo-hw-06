from task1 import create_graph, analyze_graph, visualize_graph

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    unvisited = set(graph.nodes)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


if __name__ == "__main__":
    G = create_graph(weighted=True)
    start_node = "A"

    shortest_paths = dijkstra(G, start_node)

    print(f"Shortest paths from {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"Distance to {node}: {distance}")

    analyze_graph(G)
    visualize_graph(G)