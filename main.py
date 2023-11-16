from numpy import genfromtxt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx


# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/representing-graphs-in-code/

def createg(G, matrix):
    for i in range(len(matrix)):
        G.add_node(i)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i, j] == 1:
                G.add_edge(i, j)
    return G



csv = genfromtxt('matrix.csv', delimiter=',')
matrix = csv[1:, 1:]

test = matrix.transpose()
if np.array_equal(matrix, test):
    print("grafo orientato")
    G = nx.DiGraph()
    createg(G, matrix)
    nx.draw(G, with_labels=True, arrows=True)
    plt.show()
else:
    G = nx.Graph()
    createg(G, matrix)
    nx.draw(G, with_labels=True, arrows=True)
    plt.show()
    print("non orientato")
