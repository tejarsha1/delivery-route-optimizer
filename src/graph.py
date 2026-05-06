import csv

def load_graph(file_path):

    graph = {}

    with open(file_path, mode='r') as file:

        reader = csv.DictReader(file)

        for row in reader:

            source = row['Source']
            destination = row['Destination']
            distance = int(row['Distance'])

            if source not in graph:
                graph[source] = []

            if destination not in graph:
                graph[destination] = []

            graph[source].append((destination, distance))
            graph[destination].append((source, distance))

    return graph