from typing import List
import networkx as nx


def find_cycle_in_consumption_graph(allocation: List[List[float]]):
    Graph = nx.DiGraph()
    # len(allocation) represent the people and len(allocation[0]) represents the items that are devided
    # here we put them in graph ...
    Graph.add_nodes_from(item for item in range(len(allocation) + len(allocation[0])))

    # Check if element in row  i and colum j is a partition of item j that the person i gets.
    for i in range(len(allocation)):
        for j in range(len(allocation[0])):
            if allocation[i][j] > 0:
                Graph.add_edge(i, len(allocation) + j)

    # if cycle is available in graph print it
    # otherwise print " No cycle in Graph"
    try:
        Graph_cycle = list(nx.find_cycle(Graph, orientation="ignore"))
        print("The cycle is:\t", Graph_cycle)

    except nx.NetworkXNoCycle:
        print("No cycle in Graph")
