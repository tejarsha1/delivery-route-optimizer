from graph import load_graph
from optimizer import optimize_delivery_route, generate_random_route


def main():

    graph = load_graph("../data/delivery_network.csv")

    optimized_route, optimized_distance = optimize_delivery_route(graph, "Warehouse")

    random_route, random_distance = generate_random_route(graph, "Warehouse")

    print("\nOptimized Delivery Route\n")
    print(" -> ".join(optimized_route))
    print(f"\nOptimized Distance: {optimized_distance}")

    print("\nRandom Delivery Route\n")
    print(" -> ".join(random_route))
    print(f"\nRandom Distance: {random_distance}")

    print("\nDistance Saved:", random_distance - optimized_distance)
    improvement = ((random_distance - optimized_distance) / random_distance) * 100

    print(f"Efficiency Improvement: {improvement:.2f}%")    

if __name__ == "__main__":
    main()