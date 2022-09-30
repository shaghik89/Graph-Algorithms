# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 13:56:06 2022

@author: Shaghik
"""

import networkx as nx
import matplotlib.pyplot as plt
import json
from itertools import combinations
import random
  
class graph_features:
    
    @staticmethod 
    #For computing line graph of simple connected graph
    def line_graph(graph):
        
        graph = graph
        vertices = []
        edges = []
        line_graph_vertices = []
        
        # For creating a list of vertices, edges and vertices of line graph 
        for node,neighbors in graph.items():
            for i in range(0,len(neighbors)):
                if {node,neighbors[i]} not in edges and {neighbors[i],node} not in edges:
                    edges.append({node,neighbors[i]})   
                    line_graph_vertices.append((''.join(node+neighbors[i]),sorted(''.join(node+neighbors[i]))))
            vertices.append(node) 
            
        # Creating original graph G = (vertices,edges)
        G = nx.Graph()
        G.add_nodes_from(vertices)
        for i in vertices:
            for j in vertices:
                if {i,j} in edges:
                    G.add_edge(i,j)
        nx.draw(G,with_labels=True)
        plt.show()
                     
        # Creating line graph from original graph
        H = nx.Graph()
        for i in line_graph_vertices:
            H.add_node(i[0])
        for i in line_graph_vertices:
            for j in line_graph_vertices:
                if i!=j:
                    for k in i[1]:
                        if k in j[1]:
                            H.add_edge(i[0],j[0])  
        nx.draw(H,with_labels=True)
        plt.show()
        
        print('Vertex set of original graph : ',vertices)
        print()
        print('Edge set of original graph : ',edges)
        print()
        print('Line graph vertices : ')   
        
        Line_graph_vertices = []
        for i in line_graph_vertices:
            Line_graph_vertices.append(i[0])
        return Line_graph_vertices
    
    @staticmethod 
    #Renders k_tree and partial k_tree 
    def k_tree(k,m):
        G = nx.complete_graph(k+1)
        x = list(combinations(list(range(k+1)),k))
        y = list(range(k+1,m+k+1))
        G.add_nodes_from(y)
        for i in range(k+1,m+k+1):
            xr = random.choice(x)
            for k in xr:
                G.add_edge(i,k)

        #Checks mathematical consistency
        if G.number_of_edges()==k*(k+1+m)-int(k*(k+1)/2):
            nx.draw(G,with_labels=True)
            plt.show()
    
if __name__=='__main__':
    #We pass input as dictionary. Eg : {"a":["b","d"],"b":["c","a","d"],"c":["b","d"],"d":["b","c","a"]}
    x = int(input('Which feature you want\n\n1. Line Graph\n\n2. k-tree \n \n'))
    obj = graph_features()
    if x==1:
        dict_graph = input('Enter the neighborhood of all the graph vertices \n \n ')
        print(obj.line_graph(json.loads(dict_graph)))
    elif x==2:
        y = int(input('Value of k in k-tree : '))
        z = int(input('Additional vertices : '))
        obj.k_tree(y,z)
