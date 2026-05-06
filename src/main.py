from graph import load_graph


def print_graph(graph):
    print("\nDelivery Network Loaded Successfully\n")

    for node in graph:
        connections = []

        for neighbor, distance in graph[node]:
            connections.append(f"{neighbor}({distance})")

        print(f"{node} -> {', '.join(connections)}")


def main():
    file_path = "../data/delivery_network.csv"
    graph = load_graph(file_path)
    print_graph(graph)


if __name__ == "__main__":
    main()