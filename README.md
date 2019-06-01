# Minimum Cost Spanning Tree
Algorithmic implementation to find Minimum Spanning Tree

__Complete graph__ `G` is simple graph in which any two vertices are joined by an `edge`. A complete graph of `n` vertices will have `n(n-1)/2` edges. A complete graph with `8` nodes looks like this,

![complete](https://user-images.githubusercontent.com/26320981/57195191-7fef0500-6f6d-11e9-991d-e9805fa16989.png)

__Spanning tree__ `H` is an acyclic graph whose length of `V(H) = V(G)` and `E(H)` is subset of `E(G)`, where `G` is any given graph. A spanning tree of above graph looks like this,

![spanning](https://user-images.githubusercontent.com/26320981/57195262-16232b00-6f6e-11e9-835c-ac98268b3bb4.png)

Now if we assign weights (certain integer) to edges of graph `G` then `G` becomes a weighted graph. This opens to certain problems or ideas to find __`minimum cost spanning tree`__ of graph `G`.

To find minimum cost spanning tree, we implement different algorithms such as,

* __`Kruskal's Algorithm`__
* __`Prim's Algorithm`__

Before that, we need to attain familiarity with `weighted graphs`.

__Weighted graph__ is a graph in which a real number is assigned to every edge of it. The real number is called the `weight` of the edge and is denoted by `w(e)`. For a graph of `6`, the random weights can be like this,
```
[(1, 1, {'weight': 0})]   [(3, 3, {'weight': 0})]
[(1, 2, {'weight': 13})]  [(3, 4, {'weight': 36})]
[(1, 3, {'weight': 9})]   [(3, 5, {'weight': 17})]
[(1, 4, {'weight': 44})]  [(3, 6, {'weight': 34})]
[(1, 5, {'weight': 31})]  [(4, 4, {'weight': 0})]
[(1, 6, {'weight': 28})]  [(4, 5, {'weight': 34})]
[(2, 2, {'weight': 0})]   [(4, 6, {'weight': 17})]
[(2, 3, {'weight': 47})]  [(5, 5, {'weight': 0})]
[(2, 4, {'weight': 41})]  [(5, 6, {'weight': 43})]
[(2, 5, {'weight': 34})]  [(6, 6, {'weight': 0})]
[(2, 6, {'weight': 19})]
```
the key idea is, when the graph is `underlying` (absence of directions), then the weight of `edge(a, b) = edge(b, a)`.

Working on __Cycles__ (in progress).
