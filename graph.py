import networkx as nx
import matplotlib.pyplot as plt
import json

data = json.load(open('./dicionario_final.json'))

G = nx.Graph()

edges = data.get("POLITICS", [])
print(len(edges))

for edge in edges:
    G.add_edge(*edge)

# nx.draw(G, with_labels=True)
# plt.show()

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# print("Nodes:", G.nodes())

def calculate_degree_centrality(G):
    # Calculate the degree centrality of the nodes
    centrality = nx.degree_centrality(G)
    return centrality

def calculate_closeness_centrality(G):
    # Calculate the closeness centrality of the nodes
    centrality = nx.closeness_centrality(G)
    return centrality

# Example usage
centrality = calculate_degree_centrality(G)
print("Degree Centrality:", centrality)

# Step 2: Sort Nodes by Centrality
sorted_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)

# Step 3: Select Top Nodes (at least 10)
top_nodes = [node for node, _ in sorted_nodes[:10]]

# Step 4: Create a Subgraph
subG = G.subgraph(top_nodes)

# Step 5: Plot the Graph
plt.figure(figsize=(10, 8))
nx.draw(subG, with_labels=True, node_size=700, node_color='skyblue', font_size=15, font_weight='bold')
plt.title("Top 10 Nodes by Degree Centrality")
plt.show()

# Assuming G is your graph

# Calculate Node Positions for the entire graph G
pos = nx.spring_layout(G)

# Find the Center of the Graph
center_nodes = nx.center(G)

# Plot the Graph
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=15, font_weight='bold')

# Highlight the Center Nodes
nx.draw_networkx_nodes(G, pos, nodelist=center_nodes, node_size=800, node_color='red')

plt.title("Graph G with Center Highlighted")
plt.show()