#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:00:53 2022

@author: pritomtanvir
"""

inputString = input("Please give your input: ")
algorithm_Type = inputString[-1:]
inputString = inputString[:-2]
inputList = []

while(inputString):
    inputList.append(inputString[:2])
    inputString = inputString[2:]


####bfs variables
fringeList = [inputList]
fringeListFlip = [-1]
fringeListPred = [[]]
closedSet = []
listExploredPred = []
ListExploredFlip = []

def ifSorted(lis):
    if(lis[0] == "1w" and lis[1] == "2w" and lis[2] == "3w" and lis[3] == "4w"):
        return True
    else:
        False

def flip(lis, length):
    flippedList = lis[:]
    temp ="z"
    for i in range(0, length+1):
        flippedList[i] = flippedList[i].replace("b", temp)
        flippedList[i] = flippedList[i].replace("w", "b")
        flippedList[i] = flippedList[i].replace(temp, "w")
    
    i = 0
    while(i<=length):
        temp = flippedList[i]
        flippedList[i] = flippedList[length]
        flippedList[length] = temp
        i = i + 1
        length = length-1 
        
    return flippedList

def bfsExpansion(lis):
    for i in range(len(lis)):
        flippedList = flip(lis, i)
        if(flippedList in closedSet):
            pass
        else:
            fringeList.append(flippedList)
            fringeListPred.append(lis)
            fringeListFlip.append(i+1)
        i = i +1 

def bfsPrint():
    length1 = len(closedSet) -1 
    printList = []
    flipList = []
    while(length1 >= 0):
        flipList.append(ListExploredFlip[length1])
        printList.append(closedSet[length1])
        pred = listExploredPred[length1]
        if(len(pred)!=0):
            length1 = closedSet.index(pred)
        else:
            break 
    printList = printList[::-1]
    flipList = flipList[::-1]
    length2 = len(printList) -1 
    for i in range(length2):
        printList[i].insert(flipList[i+1], "|")
        
    for i in range(length2+1):
        printList[i] = "".join(printList[i])
        print(printList[i])

def bfsAlgo():
    while(len(fringeList)):
        index = 0
        closedSet.append(fringeList[index])
        listExploredPred.append(fringeListPred[index])
        ListExploredFlip.append(fringeListFlip[index])
        
        if(ifSorted(fringeList[index])):
            print("\n")
            print("the calculated bfs output is: ")
            bfsPrint()
            break
        else:
            bfsExpansion(fringeList[index])
            fringeList.pop(index)
            fringeListPred.pop(index)
            fringeListFlip.pop(index)
        

if(algorithm_Type == "b"):
    print("calling bfs")
    bfsAlgo()
   
#**************************
#astar starts from here



def aStarExpansion(lis, gVal):
    length1AS = len(lis)
    for i in range(length1AS):
        flippedList = flip(lis, i)
        if(flippedList in closedSetAS):
            pass
        else:
            fringeListAS.append(flippedList)
            fringeListPredAS.append(lis)
            fringeListFlipAS.append(i+1)
            val = functionHAS(flippedList)
            fringeHAS.append(val)
            fringeGAS.append(i+1 +gVal)
            fringeFAS.append(val + 1 +i+ gVal)
        i = i+1

def functionHAS(lis):
    if("4" not in lis[3][0]):
    #if(!(lis[3][0].find("4")))
        return 4
    elif("3" not in lis[2][0]):
        return 3
    elif("2" not in lis[1][0]):
        return 2
    elif("1" not in lis[0][0]):
        return 1
    else:
        return 0

def aStarPrint():
    length = len(closedSetAS)-1
    printListAS = []
    flipListAS = []
    while(length >= 0):
        flipListAS.append(flipExploredAS[length])
        stringG = str(exploredGAS[length])
        stringH = str(exploredHAS[length])
        closedSetAS[length].append(" g:" + stringG+ " h: " + stringH)
        printListAS.append(closedSetAS[length])
        
        predAS = listExploredPredAS[length]
        if(len(predAS)!= 0):
            length = closedSetAS.index(predAS)
        else:
            break 
        
    printListAS = printListAS[::-1]
    flipListAS =flipListAS[::-1]
    length2AS = len(printListAS)
    for i in range(length2AS -1):
        printListAS[i].insert(flipListAS[i+1], "|")
    for i in range(length2AS):
        printListAS[i] = "".join(printListAS[i])
        print(printListAS[i])

      
    
def aStarAlgo():
    while(len(fringeListAS)):
        lis = []
        listIndex = []
        fringeFMin = min(fringeFAS)
        #print(fringeFMin)
        for i in range(len(fringeFAS)):
            if(fringeFAS[i] == fringeFMin):
                lis.append(fringeListAS[i])
                listIndex.append(i)
        index = listIndex[lis.index(max(lis))]
        
        closedSetAS.append(fringeListAS[index])
        listExploredPredAS.append(fringeListPredAS[index])
        flipExploredAS.append(fringeListFlipAS[index])
        exploredHAS.append(fringeHAS[index])
        exploredGAS.append(fringeGAS[index])
        
        if(ifSorted(fringeListAS[index])):
            print("\n")
            print("The calculated output is: ")
            aStarPrint()
            break 
        else: 
            aStarExpansion(fringeListAS[index],fringeGAS[index])
            fringeListAS.pop(index)
            fringeListPredAS.pop(index)
            fringeListFlipAS.pop(index)
            fringeHAS.pop(index)
            fringeGAS.pop(index)
            fringeFAS.pop(index)
            
        
fringeListAS = [inputList]
#print(fringeListAS)
fringeHAS = [functionHAS(inputList)]
fringeGAS = [0]
fringeFAS = [functionHAS(inputList)]
fringeListFlipAS = [-1]
fringeListPredAS = [[]]
closedSetAS = []
listExploredPredAS = []
exploredHAS = []
exploredGAS = []
flipExploredAS = []

if(algorithm_Type == "a"):
    print("calling aStar")
    aStarAlgo()