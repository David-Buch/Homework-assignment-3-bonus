import networkx as nx
import random
import matplotlib.pyplot as plt


def algorithm(graph, max_degree):
    colors = set(range(max_degree + 1))
    
    color_map = {node: -1 for node in graph.nodes}
    i = 0
    while -1 in color_map.values():
        i += 1
        candidate_map = color_map.copy() #otherwise the it would be the same object 

        for node in list(graph):  # https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.nodes.html
            if color_map[node] == -1:  
                neighbor_colors = {color_map[n] for n in graph.neighbors(node)} #https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.neighbors.html
                available_colors = colors - neighbor_colors          
                candidate = random.choice(list(available_colors))
                candidate_map[node] = candidate
                
        for node in list(graph):
            if color_map[node] == -1:        
                neighbor_candidates = [candidate_map[n] for n in graph.neighbors(node)]
                candidate = candidate_map[node]
                
                if candidate not in neighbor_candidates:
                    color_map[node] = candidate
    
    print(f"Itterations it took to get to this result: {i}, max degree: {max_degree}")
    return color_map

G = nx.binomial_graph(100, 0.2)  
max_degree = max(dict(G.degree).values())
coloring = algorithm(G, max_degree)

color_map = [coloring[node] for node in G.nodes()]
nx.draw(G, node_color=color_map, with_labels=True)
plt.show()