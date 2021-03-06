#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:45:06 2018

@author: Jiawei Zhong
"""

# Read the file and store the nodes into dictionary
f = open("graph.txt")
arr = []
nodes = {}
i = 0
for line in f.readlines():
    line = line.strip()
    temp = line.split(", ")
    if not temp[0] in nodes:
        nodes[temp[0]] = i
        i = i + 1
    if not temp[1] in nodes:
        nodes[temp[1]] = i
        i = i + 1
    arr.append(temp)
f.close()
size = len(nodes)

# Initialize an adjacent matrix and number of edges
# matrix_adj = np.zeros([size, size], dtype = int)
edgeNum = 0
matrix_adj = [[0]*size for q in range(size)]
for i in range(0, len(arr)):
    a = nodes[arr[i][0]]
    b = nodes[arr[i][1]]
    matrix_adj[a][b] = matrix_adj[a][b] + 1
    edgeNum = edgeNum + 1
print(len(nodes))
print(edgeNum)