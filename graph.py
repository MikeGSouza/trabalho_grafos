import networkx as nx
import matplotlib.pyplot as plt
import json
import random

data = json.load(open('./dict_relacoes.json'))

G = nx.Graph()

edges = data.get("POLITICS", [])

# Selecionar 100 arestas aleatórias
random_edges = random.sample(edges, 100)

for edge in random_edges:
    G.add_edge(*edge)

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

def calculate_degree_centrality(G):
    # Calculate the degree centrality of the nodes
    centrality = nx.degree_centrality(G)
    return centrality

def calculate_closeness_centrality(G):
    # Calculate the closeness centrality of the nodes
    centrality = nx.closeness_centrality(G)
    return centrality

# Example usage
degree_centrality = calculate_degree_centrality(G)
closeness_centrality = calculate_closeness_centrality(G)
print("Degree Centrality:", degree_centrality)
print("Closeness Centrality:", closeness_centrality)

# Step 5: Plot the Graph
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_size=600, node_color='skyblue', font_size=5, font_weight='bold')
plt.title("Top 10 Nodes by Degree Centrality")
plt.show()
