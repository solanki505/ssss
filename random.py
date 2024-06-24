import networkx as nx
import matplotlib.pyplot as plt
import random

def create_complete_graph(num_nodes):
    G = nx.complete_graph(num_nodes)
    return G

def draw_graph(graph):
    nx.draw(graph, with_labels=True)
    plt.show()

# Example usage
num_nodes = 2000
complete_graph = create_complete_graph(num_nodes)
draw_graph(complete_graph)

def select_random_nodes(graph, n):
    nodes = list(graph.nodes)
    random_nodes = random.sample(nodes, n)
    return random_nodes

num_nodes = 2000
complete_graph = create_complete_graph(num_nodes)
random_nodes = select_random_nodes(complete_graph, 20)
print(random_nodes)