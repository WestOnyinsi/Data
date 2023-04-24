# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 01:03:29 2022

@author: Westy
"""

class Environment():
    myGraph = {
        "GATE A": set(["ADMIN BLOCK", "LECTURER OFFICES"]),
        "ADMIN BLOCK": set(["LILLIAN BEAM"]),
        "LILLIAN BEAM": set(["CAFETERIA", "LIBRARY", "CSOB"]),
        "CAFETERIA": set(["LILLIAN BEAM", "HOSTELS", "LIBRARY", "CSOB"]),
        "LECTURER OFFICES": set(["CSOB", "GATE A"]),
        "CSOB": set(["LILLIAN BEAM", "LIBRARY", "CAFETERIA", "LECTURER OFFICES"]),
        "LIBRARY": set(["AUDITORIUM", "LILLIAN BEAM", "STUDENT CENTER", "CSOB", "CAFETERIA", "SST", "HOSTELS"]),
        "HOSTELS": set(["CAFETERIA", "STUDENT CENTER", "AUDITORIUM", "LIBRARY"]),
        "AUDITORIUM": set(["HOSTELS", "STUDENT CENTER", "LIBRARY"]),
        "STUDENT CENTER": set(["HOSTELS", "AUDITORIUM", "LIBRARY", "SST"]),
        "SST": set(["STUDENT CENTER", "LIBRARY", "SHSS"]),
        "SHSS": set(["SST", "GATE B"]),
        "GATE B": set(["SHSS"])
        }

    cost = {str(["GATE A", "ADMIN BLOCK"]): "142", str(["GATE A", "LECTURER OFFICES"]): "150", 
            
            str(["ADMIN BLOCK", "LILLIAN BEAM"]): "13",
            
            str(["LILLIAN BEAM", "CAFETERIA"]): "93", str(["LILLIAN BEAM", "LIBRARY"]): "258", str(["LILLIAN BEAM", "CSOB"]): "190",
            
            str(["CAFETERIA", "LILLIAN BEAM"]): "93", str(["CAFETERIA", "HOSTELS"]): "52", str(["CAFETERIA", "LIBRARY"]): "158", str(["CAFETERIA", "CSOB"]): "152",
           
            str(["LECTURER OFFICES", "CSOB"]): "180", str(["LECTURER OFFICES", "GATE A"]): "150",
            
            str(["CSOB", "LILLIAN BEAM"]): "190", str(["CSOB", "LIBRARY"]): "140", str(["CSOB", "CAFETERIA"]): "152", str(["CSOB", "LECTURER OFFICES"]): "180",
            
            str(["LIBRARY", "AUDITORIUM"]): "100", str(["LIBRARY", "LILLIAN BEAM"]): "258", str(["LIBRARY", "STUDENT CENTER"]): "260", str(["LIBRARY", "CSOB"]): "140", str(["LIBRARY", "CAFETERIA"]): "158", str(["LIBRARY", "SST"]): "270", str(["LIBRARY", "HOSTELS"]): "122",
            
            str(["HOSTELS", "CAFETERIA"]): "52", str(["HOSTELS", "STUDENT CENTER"]): "214", str(["HOSTELS", "AUDITORIUM"]): "83", str(["HOSTELS", "LIBRARY"]): "122",
            
            str(["AUDITORIUM", "HOSTELS"]): "83", str(["AUDITORIUM", "STUDENT CENTER"]): "140", str(["AUDITORIUM", "LIBRARY"]): "100",
            
            str(["STUDENT CENTER", "HOSTELS"]): "214", str(["STUDENT CENTER", "AUDITORIUM"]): "140", str(["STUDENT CENTER", "LIBRARY"]): "260", str(["STUDENT CENTER", "SST"]): "170",
            
            str(["SST", "STUDENT CENTER"]): "170", str(["SST", "LIBRARY"]): "270", str(["SST", "SHSS"]): "230",
            
            str(["SHSS", "SST"]): "230", str(["SHSS", "GATE B"]): "140",  
            
            str(["GATE B", "SHSS"]): "140",

            
            }
    print ("Location list:\n GATE A\n GATE B\n ADMIN BLOCK\n LILLIAN BEAM\n CAFETERIA\n LECTURER OFFICES\n CSOB\n LIBRARY\n HOSTELS\n AUDITORIUM\n STUDENT CENTER\n SST\n SHSS\n")
    x= input("Enter your current location: ")
    y= input("Enter your destination: ")
    
    
    
    start = x
    goal = y

class Agent(Environment):
    #DFS--> Depth First Search
    def DFS(graph,start,goal):
        stack = [(start, [start])]
        p = []
        while stack:
            (vertex ,path)=stack.pop() #vertex is the position and path is the contents
            for next in graph[vertex]-set(path):# remove position in graph that have been visited before
                if next == goal:
                    p.append(path+[next])
                else:
                    stack.append((next, path+[next]))
        return p


    def __init__(self, Environment):
        print("DFS", Agent.DFS(Environment.myGraph, Environment.start, Environment.goal))
        

theEnvironment = Environment()
theAgent = Agent(theEnvironment)

