import warnings
warnings.filterwarnings('ignore')
import math
import random

import numpy as np
from matplotlib import pyplot as plt
import networkx as nx


def cycles_in_random_graph(num_nodes):
    """This method detects the presence of cycle in graph.

    Parameters
    ----------
    num_nodes : no. of nodes in a graph
        Nodes are also called as vertices. 
        It takes integer values and set of vertices 
        is denoted as V(G).

    Returns True and cyclic path, if cycles detected.

    Conditions
    ----------
    > Start vertex and End vertex are same in a cycle.
    > Atleast three vertices are required to form a cycle.
    > Along the cycle, every vertex has degree 2."""

    plt.figure(figsize=(6, 5))

    nodelist = list(range(1, num_nodes + 1))
    edgelist = [(i, j) for i in nodelist for j in nodelist]

    p = 0
    eff_edgelist = []
    while p < len(edgelist):
        if edgelist[p][0] < edgelist[p][1]:
            eff_edgelist.append(edgelist[p])
        p += 1

    G = nx.Graph()
    G.add_nodes_from(nodelist)
    G.add_edges_from(eff_edgelist)
    nx.draw_circular(
        G, node_shape='s', node_color='orange', with_labels=1)
    plt.show()

    for i in G:
        print(G.degree(i))
    return None

if __name__ == '__main__':
    cycles_in_random_graph(5)
