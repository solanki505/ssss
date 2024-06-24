import networkx as nx
import matplotlib.pyplot as plt

# Function to create a complete graph with 'n' nodes and embed a watermark
def complete_graph_with_watermark(n, watermark_nodes):
    graph = nx.complete_graph(n)
    # Embed watermark on specified nodes
    for node in watermark_nodes:
        if node < n:  # Ensure the node exists in the graph
            graph.nodes[node]['watermark'] = True
    return graph

# Function to visualize the graph with watermark nodes highlighted
def visualize_graph(graph, watermark_nodes):
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(graph)  # Position nodes using spring layout

    # Determine node colors
    node_colors = ['red' if graph.nodes[node].get('watermark', False) else 'lightblue' for node in graph.nodes]

# Draw the graph with custom node colors
    nx.draw(graph, pos, with_labels=True, node_color=node_colors, node_size=800, font_size=10, font_weight='bold')
    plt.title('Scan Cell Graph (Complete) with Watermarked Nodes')
    plt.show()

# Main function to create and visualize the graph
def main():
    # Number of nodes in the scan cell graph
    num_nodes = 20

    # Nodes to embed the watermark on (3rd and 4th nodes, 0-based index)
    watermark_nodes = [2, 3]

    # Create a complete graph with watermark
    graph = complete_graph_with_watermark(num_nodes, watermark_nodes)

    # Visualize the graph with watermarked nodes
    visualize_graph(graph, watermark_nodes)

if __name__ == "__main__":
  main()