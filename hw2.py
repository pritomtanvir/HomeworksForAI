#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 19:45:01 2022

@author: pritomtanvir
"""

class Node:
    def __init__(self, state = None, value =None, left =None, centre =None
                 , right= None, index =None):
        self.state  = state
        self.value  = value 
        self.left   = left
        self.centre = centre
        self.right  = right 
        self.index  = index
        
def value(node, alpha, beta):
    if node == None:
        return None
    if node.state == "terminal":
        indList.pop(indList.index(node.index))
        return node.value
    elif node.state == "max":
       return maxValue(node, alpha, beta)
    elif node.state == "min":
       return minValue(node, alpha, beta)
    
        
def maxValue(node, alpha, beta):
        children = [node.left, node.centre, node.right]
        length = len(children)
        for i in range(length):
            l = [value(children[i], alpha, beta), node.value]
            #print("l = ", l)
            #print("max, alpha = ", alpha, "beta = ", beta, "node value = ", node.value)
            node.value = max(ind for ind in l if ind is not None)
            if(node.value >= beta):
                return node.value
            alpha = max(alpha, node.value)
        return node.value
    
    
def minValue(node, alpha, beta):
        children = [node.left, node.centre, node. right]
        length = len(children)
        for i in range(length):
            l = [value(children[i], alpha, beta), node.value]
            #print("l = ", l)
            #print("min, alpha = ", alpha, "beta = ", beta, "node value = ", node.value)
            node.value = min(ind for ind in l if ind is not None)
            if(node.value <= alpha):
                return node.value
            beta = min(beta, node.value)
        return node.value 
            

#print()
inputString = input("please enter the input: ")
terminalValue = inputString.split(" ")
#terminalValue = list(map(int, terminalValue))
terminalValue = [int(i) for i in terminalValue]
indList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
alpha = float("-inf")
beta  = float("inf")

leaf0 = Node(state = "terminal", value = terminalValue[0], index   = 0)
leaf1 = Node(state = "terminal", value = terminalValue[1], index   = 1)
leaf2 = Node(state = "terminal", value = terminalValue[2], index   = 2)
leaf3 = Node(state = "terminal", value = terminalValue[3], index   = 3)
leaf4 = Node(state = "terminal", value = terminalValue[4], index   = 4)
leaf5 = Node(state = "terminal", value = terminalValue[5], index   = 5)
leaf6 = Node(state = "terminal", value = terminalValue[6], index   = 6)
leaf7 = Node(state = "terminal", value = terminalValue[7], index   = 7)
leaf8 = Node(state = "terminal", value = terminalValue[8], index   = 8)
leaf9 = Node(state = "terminal", value = terminalValue[9], index   = 9)
leaf10 = Node(state = "terminal", value = terminalValue[10], index = 10)
leaf11 = Node(state = "terminal", value = terminalValue[11], index = 11)

node0Level2 = Node(state = "max", value = float("-inf"), left = leaf0, right =leaf1)
node1Level2 = Node(state = "max", value = float("-inf"), left = leaf2, right =leaf3)
node2Level2 = Node(state = "max", value = float("-inf"), left = leaf4, right =leaf5)
node3Level2 = Node(state = "max", value = float("-inf"), left = leaf6, right =leaf7)
node4Level2 = Node(state = "max", value = float("-inf"), left = leaf8, right =leaf9)
node5Level2 = Node(state = "max", value = float("-inf"), left = leaf10, right =leaf11)

node0Level3 = Node(state = "min", value = float("inf"), left = node0Level2, right = node1Level2)
node1Level3 = Node(state = "min", value = float("inf"), left = node2Level2, right = node3Level2)
node2Level3 = Node(state = "min", value = float("inf"), left = node4Level2, right = node5Level2)

root = Node(state = "max", value = float("-inf"), left = node0Level3, centre = node1Level3, right = node2Level3)
value(root, alpha, beta)
print("Output: ")
#print(", ".join(map(str, indList)))
print(*indList, sep=', ')




            