"""
1) Start program 
    1a) First graph will open up, press 'q' to close (make sure caps lock is not on)
    
2) Prompt will need to be answered in the terminal does not matter about caps (Answer question 1a)
    2a) Entering 'yes' will ask for the start node to enter, choose from the "nodes" list 
        2ab) Enter the traversal method, graph will show and connected components will appear in terminal 
    2b) Entering 'no' will start from generic first node ("A")
        2bb) Enter the traversal method, graph will show and connected components will appear in terminal
    2c) Prompt to perform another search 

3) Prompt for entering the source node for finding shortest path for BFS (Answers question 1b and 1c in project requirements)
    3a) Enter target node for BFS

4) Repeat 3 and 3a for DFS
    4) Green nodes are one in path, red nodes are nodes found but not in path
"""

import networkx as nx 
import matplotlib.pyplot as plt 

def create_graph(): 
    """ Creates and returns an undirected graph with predefined nodes and edges """
    G = nx.Graph() 
    
    # Nodes and edges to be added to the graph
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
    edges = [('A','B'), ('A','F'), ('A','E'), ('B','F'), ('E','F'), 
            ('B', 'C'), ('C', 'D'), ('C', 'G'), ('D','G'), ('G','J'),
            ('E','I'), ('F','I'), ('J','I'), ('I','M'), ('M', 'N'), 
            ('H', 'K'), ('H', 'L'), ('K', 'L'), ('K', 'O'), ('L', 'P')
    ]
    
    # Nodes and edges added to graph 
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    
    return G

def visualize_graph(G, pos): 
    """ 
    Visualizes the graph using specific positions for nodes

    Args:
        G (nx.Graph): The graph
        pos (dict): Positions of the nodes in the graph visualization
    """
    plt.figure(figsize=(10, 6))
    plt.title('Undirected Graph')
    nx.draw(G, pos, node_color='skyblue', node_size=800, with_labels=True)
    plt.axis('off')
    plt.show()
    
def user_defined_components(G): 
    """
    Allows user interatction for custom start node selection and displays connected components

    Args:
        G (nx.Graph): The Graph
    """
    while True: 
        # Ask the user if they want to enter a custom start node
        user_input = input("Do you want to enter a custom start node? (yes/no): ").lower()
        
        if user_input == 'yes': 
            start_node = input("Enter the start node: ").upper()
            
            if start_node not in G.nodes(): 
                print("Node does not exist in the graph. Please enter a valid node.")
                continue 
            
            # Choose a traversal method 
            method = input("Choose the traversal method (BFS/DFS): ").lower()
            if method not in ['bfs', 'dfs']: 
                print("Invalid method. Please enter 'BFS' or 'DFS'")
                continue
            
            # Finds and displays connected components from the specified start node 
            if method == 'bfs': 
                components = find_connected_components_BFS(G, start_node=start_node)
            else: 
                components = find_connected_components_DFS(G, start_node=start_node)
            
            graph_connected_components(G, components, positions, type=method)
            print(f"Connected components starting from {start_node} using {method.upper()}: {components}")
                
        elif user_input == 'no': 
            default_start_node = 'A'
            
            # Choose a traversal method 
            method = input("Choose the traversal method (BFS/DFS): ").lower()
            if method not in ['bfs', 'dfs']: 
                print("Invalid method. Please enter 'BFS' or 'DFS'")
                continue
        
            # Finds and displays connected components from the specified start node 
            if method == 'bfs': 
                components = find_connected_components_BFS(G, start_node=default_start_node)
            else: 
                components = find_connected_components_DFS(G, start_node=default_start_node)
            graph_connected_components(G, components, positions, type=method)
            print(f"Connected components starting from {default_start_node} using {method.upper()}: {components}")

        # Option to continue or stop
        continue_search = input("Do you want to perform another search? (yes/no): ").lower()
        if continue_search != 'yes': 
            break  

def find_connected_components_BFS(G, start_node=None): 
    """
    Identifies and returns the connected components of the Graph G using BFS

    Args:
        G (nx.Graph): The graph

    Returns:
        components (list of sets): a list of each set containing the nodes in a connected component
    """
    visited = set()
    components = [] 
    nodes = list(G.nodes())
    
    if start_node and start_node in G:
        # If a start node is specified, ensure it's processed first
        nodes = [start_node] + [n for n in G.nodes() if n != start_node]
    else:
        nodes = G.nodes()
    
    for node in nodes:
        if node not in visited:
            # Perform DFS from the unvisited node and record the component
            component_nodes = list(nx.bfs_tree(G, source=node))
            visited.update(component_nodes)
            components.append(component_nodes)
    
    return components
    
def find_connected_components_DFS(G, start_node=None): 
    """
    Identifies and returns the connected components of the Graph G using DFS

    Args:
        G (nx.Graph): The graph

    Returns:
        components (list of sets): a list of each set containing the nodes in a connected component
    """
    visited = set()
    components = [] 
    
    if start_node and start_node in G:
        # If a start node is specified, ensure it's processed first
        nodes = [start_node] + [n for n in G.nodes() if n != start_node]
    else:
        nodes = G.nodes()
    
    for node in nodes:
        if node not in visited:
            # Perform DFS from the unvisited node and record the component
            component_nodes = list(nx.dfs_preorder_nodes(G, source=node))
            visited.update(component_nodes)
            components.append(component_nodes)
    
    return components
    

def graph_connected_components(G, components, pos, type): 
    """
    Visualize the connected components of the graph using different colors for each component

    Args:
        G (nx.Graph): The graph
        components (_type_): _description_
        pos (dict): Positions of the nodes in the graph visualization
    """
    plt.figure(figsize=(10, 6))
    plt.title(f'Connected Components in the Graph using {type.upper()}')
    
    # Colors 
    colors = ['#C6442A', '#3CB043']
    
    # Visualize each component with a unique color
    for idx, component in enumerate(components): 
        color = colors[idx % len(colors)]
        nx.draw_networkx_nodes(G, pos, nodelist=component, node_color=color, node_size=800)
        
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_labels(G, pos)
    plt.axis('off')
    plt.show()
    
def path_using_BFS(G, pos, source_node, target_node): 
    """
    Finds and graphs the shortest path between two nodes using BFS

    Args:
        G (nx.Graph): The graph
        pos (dict): Positions of the nodes in the graph visualization
        source_node (str): The starting node of the path
        target_node (str): The ending node of the path
    """
    try: 
        # Finds the shortest path using BFS 
        shortest_path = nx.shortest_path(G, source=source_node, target=target_node)
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        
        plt.figure(figsize=(10, 6))
        plt.title(f'Graph with Highlighted Path from {source_node} to {target_node}')
        
        # Draw graph with shortest path highlighted
        nx.draw(G, pos, node_color='skyblue', node_size=800, with_labels=True)
        nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='#3CB043', node_size=800)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
        plt.axis('off')
        plt.show()
        
        print(f"Shortest path from {source_node} to {target_node} using BFS: ", shortest_path)
    
    # Execption is raised if no path exists between the source and target
    except nx.NetworkXNoPath: 
        print(f"No path exists between {source_node} and {target_node}")
    
def path_using_DFS(graph, pos, source, target): 
        
    visited = set() 
    all_visited = [] 
        
    def dfs_utilities(current, path): 
        if current == target: 
            return path
            
        visited.add(current)
        all_visited.append(current)
            
        for neighbor in graph.neighbors(current): 
            if neighbor not in visited: 
                next_path = dfs_utilities(neighbor, path + [neighbor])
                if next_path: 
                    return next_path
            
        return None
        
    path = dfs_utilities(source, [source])
        
    if path: 
        path_edges = list(zip(path, path[1:]))
        all_visited_except_path = set(all_visited) - set(path)
            
        # Drawing the graph
        plt.figure(figsize=(10, 6))
        nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=800)
        nx.draw_networkx_nodes(graph, pos, nodelist=path, node_color='lightgreen', node_size=800)
        nx.draw_networkx_nodes(graph, pos, nodelist=all_visited_except_path, node_color='red', node_size=800)
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2, arrows=True, arrowsize=20)
            
        plt.title(f'DFS Path Visualization from {source} to {target}')
        plt.axis('off')
        plt.show()
            
        print(f"DFS path from {source} to {target}: {path}")
        print(f"All visited nodes: {all_visited}")
    else: 
        print(f"No path was found from {source} to {target} using DFS")
                
if __name__ == "__main__": 
    
    # defined positions for visualization
    positions = {
        'A': (-1, 1), 'B': (0, 1), 'C': (1, 1), 'D': (2, 1), 
        'E': (-1, 0), 'F': (0, 0), 'G': (1, 0), 'H': (2, 0),
        'I': (-1, -1), 'J': (0, -1), 'K': (1, -1), 'L': (2, -1),
        'M': (-1, -2), 'N': (0, -2), 'O': (1, -2), 'P': (2, -2)
    }
    
    # Create and visualizing the graph
    G = create_graph()
    visualize_graph(G, positions)
    
    # Visualize the connected components 
    user_defined_components(G)

    # Get source and target node
    source_node = input("Enter the source node to find shortest path using BFS: ")
    target_node = input("Enter the target node to find shortest path using BFS: ")
    
    # Finds path between two nodes using BFS
    path_using_BFS(G, positions, source_node, target_node)
    
    # Get source and target node
    source_node = input("Enter the source node to find shortest path using DFS: ")
    target_node = input("Enter the target node to find shortest path using DFS: ")
    
    # Finds path between two nodes using DFS
    path_using_DFS(G, positions, source_node, target_node)
