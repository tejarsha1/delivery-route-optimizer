# Delivery Route Optimizer

## Overview

This project applies graph algorithms to optimize delivery routes in a transportation network.

The system represents delivery locations as nodes in a graph and roads between locations as weighted edges. Using Dijkstra’s Algorithm, the project computes efficient delivery routes that minimize total travel distance.

The project also compares the optimized route against a randomly generated delivery route to evaluate efficiency improvements.

---

## Problem Statement

In real-world delivery systems, drivers must deliver packages to multiple locations while minimizing travel distance and transportation cost.

When routes are selected manually or randomly, drivers may travel unnecessary distances, increasing:
- fuel consumption
- delivery time
- operational cost

This project solves the problem by dynamically selecting efficient delivery routes using shortest-path computations.

---

## Dataset

The dataset is stored in:

```text
data/delivery_network.csv
```

The dataset contains:
- delivery locations
- warehouse starting point
- distances between connected locations

Example:

| Source | Destination | Distance |
|---|---|---|
| Warehouse | A | 4 |
| A | D | 5 |

---

## Algorithm Used

The project uses :contentReference[oaicite:0]{index=0} to compute shortest paths in a weighted graph.

### Graph Representation

- Nodes → delivery locations
- Edges → roads between locations
- Edge weights → travel distance

### Optimization Approach

1. Start from the warehouse
2. Run Dijkstra’s Algorithm
3. Find the nearest unvisited delivery location
4. Move to that location
5. Repeat until all locations are visited

---

## Project Structure

```text
delivery-route-optimizer/
│
├── data/
│   └── delivery_network.csv
│
├── src/
│   ├── main.py
│   ├── graph.py
│   ├── dijkstra.py
│   └── optimizer.py
│
├── proposal/
├── presentation/
├── README.md
└── requirements.txt
```

---

## How to Run

### Step 1

Clone the repository:

```bash
git clone <repository-url>
```

### Step 2

Move into the project folder:

```bash
cd delivery-route-optimizer
```

### Step 3

Run the program:

```bash
cd src
python3 main.py
```

---

## Example Output

```text
Optimized Distance: 90

Random Distance: 267

Distance Saved: 177

Efficiency Improvement: 66.29%
```

---

## Results

The optimized delivery route significantly reduced total travel distance compared to a random delivery route.

The system achieved:
- lower travel distance
- improved route efficiency
- reduced unnecessary traversal

---

## AI Usage Statement

AI tools were used only for guidance, formatting assistance, debugging support, and improving documentation clarity.

All core logic, implementation, project structure, and algorithm development were manually written and implemented.

---