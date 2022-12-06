
from Q3 import find_cycle_in_consumption_graph

if __name__ == '__main__':
    # no cycle available
    ex1 = [[0.85, 0.0, 0.0],
           [0.15, 0.0, 0.0],
           [0.0, 0.5, 1.0]]
    find_cycle_in_consumption_graph(ex1)

    ex2 = [[0.8, 0.0, 0.0],
           [0.2, 0.0, 2.0],
           [0.0, 0.5, 1.0]]
    find_cycle_in_consumption_graph(ex2)
    # cycle is available
    ex3 = [[0.0, 0.7, 1.0],
           [0.15, 0.3, 1.0],
           [0.85, 0.0, 0.0]]

    find_cycle_in_consumption_graph(ex3)

    ex4 = [[0.0, 0.5, 1.0],
           [0.85, 0.0, 0.0],
           [0.15, 0.5, 1.0]]

    find_cycle_in_consumption_graph(ex4)

    ex5 = [[0.0, 0.5, 1.0, 0.2],
           [0.85, 0.0, 0.0, 0.8],
           [0.15, 0.5, 1.0, 0.0],
           [0.0, 0.0, 0.0, 0.0]]

    find_cycle_in_consumption_graph(ex5)
