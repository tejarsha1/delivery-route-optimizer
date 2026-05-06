from graph import load_graph
from optimizer import optimize_delivery_route


def main():

    graph = load_graph("../data/delivery_network.csv")

    route, total_distance = optimize_delivery_route(graph, "Warehouse")

    print("\nOptimized Delivery Route\n")

    print(" -> ".join(route))

    print(f"\nTotal Distance: {total_distance}")


if __name__ == "__main__":
    main()