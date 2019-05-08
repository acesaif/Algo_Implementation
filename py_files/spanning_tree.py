import warnings
warnings.filterwarnings('ignore')
import math
import random

import numpy as np
from matplotlib import pyplot as plt
import networkx as nx


def define_random_tree(num_nodes, num_edges):
    """This method draws a random tree based on 
    given parameters.

    Parameters
    ----------
    num_nodes : no. of nodes in a graph
        Nodes are also called as vertices. 
        It takes integer values and set of vertices 
        is denoted as V(G).
    num_edges : no. of edges in a graph
        Edges are also called as links. 
        It takes integer values and set of edges 
        is denoted as E(G)."""

    plt.figure(figsize=(6, 5))

    nodelist = [i for i in range(1, num_nodes + 1)]
    edgelist = [(i, random.randint(i, num_nodes)) 
                for i in range(1, num_edges + 1)]

    G = nx.Graph()
    G.add_nodes_from(nodelist)
    G.add_edges_from(edgelist)
    nx.draw_circular(
        G, node_shape='s', node_color='orange', with_labels=1)
    plt.show()
    return None


class SpanningTree(object):
    """Spanning tree of complete graph."""

    def __init__(self, num_nodes, num_edges):
        self.num_nodes = num_nodes
        self.num_edges = num_edges

    def fetchCompleteGraph(self):
        """This method obtains a complete graph, 
        based on no. nodes mentioned."""

        plt.figure(figsize=(6, 5))

        nodelist = list(range(1, self.num_nodes + 1))
        edgelist = []
        for i in nodelist:
            for j in nodelist:
                edgelist.append((i, j))

        G = nx.Graph()
        G.add_nodes_from(nodelist)
        G.add_edges_from(edgelist)
        nx.draw_circular(G, node_shape='s', 
                node_color='orange', with_labels=1)
        plt.title("A Complete Graph of {}".format(self.num_nodes))
        plt.show()
        return None

    def fetchSpanningTree(self):
        """This method obtains a randomized spanning tree 
        of a complete graph, which is based on no. of nodes."""

        plt.figure(figsize=(6, 5))

        nodelist = list(range(1, self.num_nodes + 1))
        edgelist = [(i, random.randint(i, self.num_nodes)) 
                    for i in range(1, self.num_edges + 1)]

        G = nx.Graph()
        G.add_nodes_from(nodelist)
        G.add_edges_from(edgelist)
        nx.draw_circular(G, node_shape='s', 
                         node_color='orange', with_labels=1)
        plt.title("A Spanning Tree of {}".format(self.num_nodes))
        plt.show()
        return None


if __name__ == "__main__":
    define_random_tree(10, 10)

    graph = SpanningTree(8, 8)
    graph.fetchCompleteGraph()
    graph.fetchSpanningTree()
