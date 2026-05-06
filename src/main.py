from graph import load_graph
from dijkstra import dijkstra, get_shortest_path


def main():
    graph = load_graph("../data/delivery_network.csv")

    distances, previous = dijkstra(graph, "Warehouse")

    destination = "T"
    path = get_shortest_path(previous, "Warehouse", destination)

    print("Shortest path from Warehouse to", destination)
    print("Path:", " -> ".join(path))
    print("Distance:", distances[destination])


if __name__ == "__main__":
    main()