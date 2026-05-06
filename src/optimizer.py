from dijkstra import dijkstra


def optimize_delivery_route(graph, start):

    unvisited = set(graph.keys())
    unvisited.remove(start)

    current_location = start

    route = [start]
    total_distance = 0

    while unvisited:

        distances, _ = dijkstra(graph, current_location)

        nearest_location = None
        shortest_distance = float('inf')

        for location in unvisited:

            if distances[location] < shortest_distance:
                shortest_distance = distances[location]
                nearest_location = location

        route.append(nearest_location)

        total_distance += shortest_distance

        current_location = nearest_location

        unvisited.remove(nearest_location)

    return route, total_distance