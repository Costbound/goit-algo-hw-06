from task1 import create_graph, analyze_graph, visualize_graph

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


if __name__ == "__main__":
    G = create_graph()
    start_node = "A"
    goal_node = "E"

    dfs_paths = list(dfs_path(G, start_node, goal_node))
    bfs_paths = list(bfs_path(G, start_node, goal_node))

    print("DFS paths from A to E:")
    for path in dfs_paths:
        print(path)

    print("\nBFS paths from A to E:")
    for path in bfs_paths:
        print(path)

    analyze_graph(G)
    visualize_graph(G)