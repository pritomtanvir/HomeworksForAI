#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 01:43:58 2022

@author: pritomtanvir
"""
import random 
random.seed(1)

normal = 0 
goal = 1
forbidden = 2
wall = 3

directions = {'up': (-1, 0), 'right': (0,1), 'left':(0, -1), 'down': (1,0), }
policy = ['up', 'right', 'left', 'down']

start_x = 3
start_y = 1
gamma = 0.1
learning_rate = 0.3 

class Node():
    def __init__(self, index):
        self.state = normal
        self.index = index
        self.q = {'up': 0.0, 'right': 0.0, 'down':0.0, 'left': 0.0}
        
    def nodeUpdate(self, **kwg):
        if 'state' in kwg:
            self.state = kwg.get('state')
        elif 'q' in kwg: 
            self.q = kwg.get('q')
    

boxes = [[Node(13), Node(14), Node(15), Node(16)],
         [Node(9), Node(10), Node(11), Node(12)],
         [Node(5), Node(6), Node(7), Node(8)],
         [Node(1), Node(2), Node(3), Node(4)]]


input_string = input()
input_list = input_string.split(" ")


boxes[3-(int(input_list[0])-1)//4][(int(input_list[0])-1)%4].nodeUpdate(state = goal)
boxes[3-(int(input_list[0])-1)//4][(int(input_list[0])-1)%4].nodeUpdate(q = {'goal': 0})

boxes[3-(int(input_list[1])-1)//4][(int(input_list[1])-1)%4].nodeUpdate(state = goal)
boxes[3-(int(input_list[1])-1)//4][(int(input_list[1])-1)%4].nodeUpdate(q = {'goal': 0})

boxes[3-(int(input_list[2])-1)//4][(int(input_list[2])-1)%4].nodeUpdate(state = forbidden)
boxes[3-(int(input_list[2])-1)//4][(int(input_list[2])-1)%4].nodeUpdate(q = {'forbid': 0})

boxes[3-(int(input_list[3])-1)//4][(int(input_list[3])-1)%4].nodeUpdate(state = wall)
boxes[3-(int(input_list[3])-1)//4][(int(input_list[3])-1)%4].nodeUpdate(q = {'wall-square': 0})


def printPolicy():
    for x in range(3, -1, -1):
        for y in range(4):
            node = boxes[x][y]
            print(node.index, max(node.q, key=node.q.get))

def printValueQ(index):
    x_tem = index -1 
    x = 3-(x_tem)//4
    y = (index - 1)%4
    q = boxes[x][y].q
    for direction, value in q.items():
        print(direction, round(value,2))

for i in range(10000):
    current_x = start_x
    current_y = start_y
    
    while(True):
        q = boxes[current_x][current_y].q
        state = boxes[current_x][current_y].state
        
        if(state == goal):
            break
        elif(state == forbidden):
            break
        elif(state == wall):
            break
        elif(state == normal):
            ran = random.random()
            if(ran > 0.6):
                action = max(q, key=q.get)
            else:
                rand = random.randint(0,3)
                if(rand == 0):
                    action = "up" 
                elif(rand == 1):
                    action = "right" 
                elif(rand == 2):
                    action = "down" 
                elif(rand == 3):
                    action = "left"

            d_pos = directions[action]

            new_x = current_x + d_pos[0]
            new_y = current_y + d_pos[1]

           
            if not (0> new_x or new_x >3 or 0> new_y or new_y >3 ):
                
                if( boxes[new_x][new_y].state == wall):
                    q[action] = (1 - learning_rate) * q[action] + learning_rate * (-0.1 + gamma * max(boxes[current_x][current_y].q.values()))
                    boxes[current_x][current_y].q = q
                elif (boxes[new_x][new_y].state == goal):
                        q[action] = 100.0
                        boxes[current_x][current_y].q = q
                        current_x = new_x
                        current_y = new_y
                elif (boxes[new_x][new_y].state == forbidden):
                        q[action] = -100.0
                        boxes[current_x][current_y].q = q
                        current_x = new_x
                        current_y = new_y
                else:
                        q[action] = (1 - learning_rate) * q[action] + learning_rate * (-0.1 + gamma * max(boxes[new_x][new_y].q.values()))
                        boxes[current_x][current_y].q = q
                        current_x = new_x
                        current_y = new_y
            else:
                q[action] = (1 - learning_rate) * q[action] + learning_rate * (-0.1 + gamma * max(boxes[current_x][current_y].q.values()))
                boxes[current_x][current_y].q = q

if ("p" in input_string):
    printPolicy()
elif("q" in input_string):
    printValueQ(int(input_list[5]))
else:
    print("error")
                
                