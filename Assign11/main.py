
import matplotlib.pyplot as plt
import networkx as nx
from typing import List


def build_graph(valuations: List[List[int]]):
    g = nx.DiGraph()
    nodes = [i for i in range(len(valuations))]
    g.add_nodes_from(nodes)
    edges = [(i, j) for i, row in enumerate(valuations) for j in range(len(valuations)) if row[j] == max(row)]
    g.add_edges_from(edges)

    # Use the spring layout algorithm to position the nodes
    pos = nx.spring_layout(g, seed=1)
    nx.draw(g, pos, with_labels=True)
    edge_labels = {(i, j): valuations[i][j] for i, j in edges}
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
    plt.show()

    return g

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    build_graph([[10,1,10,5,6],[3,50,2,3,4],[6,10,3,10,1], [1,2,3,4,5],[10,10,10,10,10]])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
