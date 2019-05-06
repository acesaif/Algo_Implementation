import warnings
warnings.filterwarnings('ignore')
import math
import random

import numpy as np
from matplotlib import pyplot as plt
import networkx as nx


def randomly_weighted_graph(num_nodes):
    """This method adds random weights to 
    each edge of the graph."""

    plt.figure(figsize=(6, 5))

    nodelist = list(range(1, num_nodes + 1))
    edgelist = []
    for i in nodelist:
        for j in nodelist:
            edgelist.append([i, j])

    p = 0
    eff_edgelist = []
    while p < len(edgelist):
        if edgelist[p][0] < edgelist[p][1]:
            eff_edgelist.append(edgelist[p])
        p += 1
    
    for i in eff_edgelist:
        i.append(random.randint(5, 50))
    eff_edgelist = [tuple(i) for i in eff_edgelist]
    
    G = nx.Graph()
    G.add_nodes_from(nodelist)
    G.add_weighted_edges_from(eff_edgelist)
    nx.draw_circular(
        G, node_shape='s', node_color='orange', with_labels=1)
    
    for i in list(G.edges(data=True)):
        print([i])
    return plt.show()

if __name__ == '__main__':
    randomly_weighted_graph(6)
