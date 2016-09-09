import networkx as nx
import matplotlib.pyplot as plt
import community
from parallel_between import plotBetweeness

G = nx.read_edgelist('newfiles.txt',create_using=nx.DiGraph(), nodetype = int)
print nx.info(G)
G = G.to_undirected()

spring_pos = nx.spring_layout(G)

nx.draw_networkx(G, pos = spring_pos, with_labels = False, node_size = 35)
#plt.show()


parts = community.best_partition(G)
values = [parts.get(node) for node in G.nodes()]
nx.draw_networkx(G, pos = spring_pos, cmap = plt.get_cmap("jet"), node_color = values, node_size = 35, with_labels = False)
#nx.draw_networkx_labels(G_betweenness,pos,font_size=12,font_color='b')
plt.show()


#plotBetweeness(G, spring_pos)
#plt.clf()