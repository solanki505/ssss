import sys
import networkx as nx
import matplotlib.pyplot as plt

def tsp(graph):
    n = len(graph)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if mask != (1 << v) and mask & (1 << v):
                        dp[mask][u] = min(dp[mask][u], dp[mask ^ (1 << u)][v] + graph[v][u])

    min_cost = min(dp[-1][u] + graph[u][0] for u in range(1, n))
    return min_cost, dp

# Example graph representing distances between cities
graph = [
  [0, 9, 13, 8, 14, 11, 12, 4, 13, 9],
    [9, 0, 10, 11, 13, 8, 11, 5, 10, 8],
    [13, 10, 0, 11, 9, 8, 11, 13, 6, 10],
    [8, 11, 11, 0, 8, 11, 10, 8, 9, 11],
    [14, 13, 9, 8, 0, 11, 12, 14, 9, 9],
    [11, 8, 8, 11, 11, 0, 13, 7, 10, 10],
    [12, 11, 11, 10, 12, 13, 0, 12, 13, 15],
    [4, 5, 13, 8, 14, 7, 12, 0, 11, 9],
    [10, 6, 9, 9, 10, 13, 11, 0, 6, 9],
    [9, 8, 10, 11, 9, 10, 15, 9, 6, 0]
 ]

# Visualization function for the graph
def visualize_graph(graph):
    G = nx.Graph()
    n = len(graph)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=graph[i][j])

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Graph Before TSP")
    plt.show()

# Visualization function for the TSP solution
def visualize_tsp_solution(graph, dp):
    n = len(graph)
    min_mask = (1 << n) - 1
    min_cost = min(dp[-1][u] + graph[u][0] for u in range(1, n))
    path = []
    mask = min_mask
    u = 0
    while mask:
        v = min(range(n), key=lambda x: dp[mask][x] + graph[x][u])
        path.append((u, v))
        mask ^= 1 << v
        u = v

    G = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=graph[i][j])

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    nx.draw_networkx_edges(G, pos, edgelist=path, edge_color='r', width=2)
    plt.title("Graph After TSP")
    plt.show()

# Visualize the original graph
visualize_graph(graph)

# Calculate the minimum cost and visualize the TSP solution
min_cost, dp = tsp(graph)
print("Minimum cost for TSP:", min_cost)
visualize_tsp_solution(graph, dp)
