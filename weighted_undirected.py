import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 
from collections import defaultdict

def create_graph(): 
    """
    Creates and returns a weighted graph with predefined nodes and edges

    Returns:
        G (nx.Graph): The Graph
    """
    # Create a graph
    G = nx.Graph()
    
    # Nodes and Edges
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'] 
    weighted_edges = [
        ('A', 'B', 22), ('A', 'C', 9), ('A', 'D', 12), ('B', 'C', 35), ('B', 'H', 34), ('B', 'F', 36),
        ('C', 'D', 4), ('C', 'E', 65),('C', 'F', 42), ('D', 'E', 33), ('D', 'I', 30), ('E', 'G', 23), 
        ('F', 'G', 39), ('F', 'E', 18), ('H', 'F', 24), ('G', 'I', 21), ('H', 'I', 19), ('H', 'G', 25)
    ]
    
    # Nodes and edges added to graph 
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(weighted_edges)
    
    return G

def visualize_graph(G, pos): 
    """ 
    Visualizes the graph using specific positions for nodes

    Args:
        G (nx.Graph): The graph
        pos (dict): Positions of the nodes in the graph visualization
    """
    plt.figure(figsize=(10, 6))
    plt.title("Weighted Undirected Graph")
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, width=2)
    
    # Draw weighted edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.show()
    
def dijkstra_shortest_paths(G, source):
    """
    Applies Dijkstra's algorithm to find the shortest paths from a source node 

    Args:
        G (nx.Graph): The graph on which to perform Dijkstra's algorithm
        source (node): The source node for shortest path calculation

    Returns:
        tuple: A tuple containing the edges in the shortest path tree, lengths of shortest path, and the paths thenselves
    """
    lengths, paths = nx.single_source_dijkstra(G, source)
    edges_in_tree = [(path[i], path[i+1]) for path in paths.values() for i in range(len(path) - 1)]
    
    return edges_in_tree, lengths, paths

def parallel_offset(x0, y0, x1, y1, offset):
    """Calculates the coordinates for a line parallel to a given line segment, offset by a specified amount

    Args:
        x0, y0 (float): Coordinates of the start point of the original line
        x1, y1 (float): Coordinates of the end point of the original line
        offset (float): Distance by which the parallel line is offset

    Returns:
        tuple: Start and end coordinates of the offset line
    """
    dx = x1 - x0
    dy = y1 - y0
    norm = np.sqrt(dx**2 + dy**2)
    ux, uy = -dy / norm, dx / norm
    return (x0 + ux * offset, y0 + uy * offset), (x1 + ux * offset, y1 + uy * offset)

def draw_shortest_path_tree_with_colors(G, pos, paths, source):
    """
    Visualizes the shortest path tree with paths colored differently

    Args:
        G (nx.Graph): The graph
        pos (dict): Node positions for visualization
        paths (dict): A dictionary of paths from the source node to every other node
        source (node): The source node for the paths
    """
    plt.figure(figsize=(12, 8))
    plt.title(f"Shortest path tree starting at {source}")
    
    # Draw the background graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, edge_color='black', width=2)

    colors = ['red', 'green', 'blue', 'purple', 'orange', 'brown', 'pink', 'olive', 'cyan', 'magenta']
    path_legends = []

    # Record the usage count of edges to determine the offset for parallel lines
    edge_usage_count = defaultdict(int)

    # Sort paths by length (longest first)
    sorted_paths = sorted(paths.items(), key=lambda item: len(item[1]), reverse=True)

    for index, (target, path) in enumerate(sorted_paths):
        # Skip source node
        if target == source:
            continue  

        color = colors[index % len(colors)]
        path_edges = list(zip(path, path[1:]))

        for edge in path_edges:
            edge_usage_count[edge] += 1
            
            # Count usage for both directions
            edge_usage_count[(edge[1], edge[0])] += 1  

            # Offset each edge based on usage count
            line_offset = (edge_usage_count[edge] - 1) * 0.02

            # Draw the parallel offset edges
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            if line_offset > 0:  
                offset_start, offset_end = parallel_offset(x0, y0, x1, y1, line_offset)
                plt.plot([offset_start[0], offset_end[0]], [offset_start[1], offset_end[1]], color=color, linewidth=2)
            else:
                plt.plot([x0, x1], [y0, y1], color=color, linewidth=2)

        path_legends.append(f"Path {source} to {target} ({color})")

    # Highlight the source node
    nx.draw_networkx_nodes(G, pos, nodelist=[source], node_size=900, node_color='skyblue')

    # Manually draw edge labels with custom space around them
    edge_labels = nx.get_edge_attributes(G, 'weight')
    for (u, v), weight in edge_labels.items():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        label_pos = ((x0 + x1) / 2, (y0 + y1) / 2)
        plt.text(label_pos[0], label_pos[1], weight, 
                 horizontalalignment='center', verticalalignment='center',
                 bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2'))

    # Create a custom legend
    custom_lines = [plt.Line2D([0], [0], color=color, lw=4) for color in colors[:len(path_legends)]]
    plt.legend(custom_lines, path_legends, fontsize='small', title="Paths", title_fontsize='medium', loc='upper left')

    plt.axis('equal')
    plt.show()
    
def visualize_minimum_spanning_tree(G, pos):
    """
    Computes and visualizes the minimum spanning tree of the graph

    Args:
        G (nx.Graph): The graph for which to compute the MST
        pos (dict): Node positions for visualization
    """
    # Compute the minimum spanning tree
    mst = nx.minimum_spanning_tree(G)

    # Calculate the total weight of the MST
    total_weight = sum(weight for (u, v, weight) in mst.edges.data('weight'))

    # Print the edges and the total weight of the MST
    print("\nMinimum Spanning Tree (MST) Details:")
    print("-------------------------------------")
    for u, v, weight in mst.edges.data('weight'):
        print(f"Edge ({u}, {v}) with weight: {weight}")
    print(f"Total weight of MST: {total_weight}")
    
    # Plot the graph
    plt.figure(figsize=(10, 6))
    plt.title('Minimum Spanning Tree')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, edge_color='gray', width=2)

    # Draw the MST edges on top of the graph
    edge_labels = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx_edges(mst, pos, edge_color='red', width=3)
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels, font_color='red')

    plt.show()


if __name__ == "__main__":
    
    # defined positions for visualization
    positions = { 
    'A': (0, 0), 'B': (1, 1), 'C': (1, 0), 
    'D': (1, -2), 'H': (4, 1), 'I': (4, -2), 
    'E': (2, -.7), 'G': (3, -.7), 'F': (2.5, .3)
    }

    G = create_graph()
    visualize_graph(G, positions)
        
    # Correctly call the function with paths dictionary
    user_selection = input("Would you like to start at a certain node (yes/no): ").lower()
    
    if user_selection == 'no': 
        # Get the shortest path tree starting from node 'A'
        edges_in_tree, lengths, paths = dijkstra_shortest_paths(G, 'A')
        
        # Print the lengths and pathsq
        print("Shortest paths from node 'A':")
        for node, length in lengths.items():
            print(f"Node {node} has a path of length {length}: {paths[node]}")
            
        draw_shortest_path_tree_with_colors(G, positions, paths, 'A')
    else: 
        specified_node = input("What node would you like start from: ").upper()

        # Get the shortest path tree starting from node 'A'
        edges_in_tree, lengths, paths = dijkstra_shortest_paths(G, specified_node)
        
        # Print the lengths and pathsq
        print(f"Shortest paths from node {specified_node}: ")
        for node, length in lengths.items():
            print(f"Node {node} has a path of length {length}: {paths[node]}")
        
        draw_shortest_path_tree_with_colors(G, positions, paths, specified_node)
    
    # Visualize the Minimum Spanning Tree
    visualize_minimum_spanning_tree(G, positions)
