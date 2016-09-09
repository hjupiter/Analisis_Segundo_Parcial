import networkx as nx
import matplotlib.pyplot as plt
from pylab import show


def most_important(G):
	ranking = nx.betweenness_centrality(G).items()
	#print ranking
	r = [x[1] for x in ranking]
	m = sum(r)/len(r) # mean centrality
	t = m*3 # threshold, we keep only the nodes with 3 times the mean
	Gt = G.copy()
	for k, v in ranking:
		if v < t:
			Gt.remove_node(k)
	return Gt

nyc_net = nx.read_edgelist('newfiles.txt',create_using=nx.DiGraph(), nodetype = int)
N,K = nyc_net.number_of_nodes(),nyc_net.number_of_edges()
nyc_net_ud = nyc_net.to_undirected()
#FIND the largest connected component
nyc_net_components = nx.connected_component_subgraphs(nyc_net_ud)
nyc_net_mc = next(nyc_net_components)
#Statas
N_mc,K_mc = nyc_net_mc.order(), nyc_net_mc.size()
avg_deg_mc = float(2*K_mc)/N_mc
avg_clust = nx.average_clustering(nyc_net_mc)


#print ""
#print "GCC (main component)"
#print "Nodes: ", N_mc
#print "Edges: ", K_mc
#print "Average degree: ", avg_deg_mc
#print "Average clustering coefficient: ", avg_clust

#Aleatoria
X = K/float(N*(N-1.0)/2.0)
G_Random = nx.erdos_renyi_graph (N,X)
G_Random_ud = G_Random.to_undirected()
G_Random_net_components = nx.connected_component_subgraphs(G_Random_ud)
G_Random_mc = next(G_Random_net_components)
G_N_mc,G_K_mc = G_Random_mc.order(), G_Random_mc.size()
G_avg_deg_mc = float(2*G_K_mc)/G_N_mc
G_avg_clust = nx.average_clustering(G_Random_mc)

#print ""
#print "GCC (main component Random)"
#print "Nodes: ", G_N_mc
#print "Edges: ", G_K_mc
#print "Average degree: ", G_avg_deg_mc
#print "Average clustering coefficient: ", G_avg_clust



#Betewwenes
print ""
print "Betweenness Centrality"
top = 10
G_H = nx.betweenness_centrality(nyc_net)
n = sorted(G_H.items(), key=lambda x: -x[1])[:top]
print "Max Key" +"\t\t" + "Max Value" 
for max_key, max_val in n:
	print str(max_key) +"\t\t" + str(max_val) 
#print G_H

#print ""
print "Eigenvector Centrality"
G_E = nx.eigenvector_centrality(nyc_net)
n = sorted(G_E.items(), key=lambda x: -x[1])[:top]
print "Max Key" +"\t\t" + "Max Value" 
for max_key, max_val in n:
	print str(max_key) +"\t\t" + str(max_val) 
#print G_E

G_betweenness = most_important(nyc_net)
#print G_betweenness.items()
pos = nx.spring_layout(nyc_net)
nx.draw_networkx_nodes(nyc_net,pos,node_color='b',alpha=0.2,node_size=8)
nx.draw_networkx_edges(nyc_net,pos,alpha=0.1)
nx.draw_networkx_nodes(G_betweenness,pos,node_color='r',alpha=0.4,node_size=254)
nx.draw_networkx_labels(G_betweenness,pos,font_size=7,font_color='b')
show()
#G_eigenvector = nx.eigenvector_centrality(nyc_net)
