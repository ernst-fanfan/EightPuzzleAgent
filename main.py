# AI Class
# Ernst Fanfan
# 2/1/2022
# Assignment 1
# Agent Creation to solve 8 puzzle
from BreathFirstSearch import BFS
from DepthFirstSearch import DFS
from EightPuzzle import SlidePuzzle

# main function
from UniformCostSearch import UCS

if __name__ == '__main__':
    # create the graph
    graph, cost = [[] for i in range(8)], {}

    # add edge
    graph[0].append(1)
    graph[0].append(3)
    graph[3].append(1)
    graph[3].append(6)
    graph[3].append(4)
    graph[1].append(6)
    graph[4].append(2)
    graph[4].append(5)
    graph[2].append(1)
    graph[5].append(2)
    graph[5].append(6)
    graph[6].append(4)
    # print(graph)
    # add the cost
    cost[(0, 1)] = 2
    cost[(0, 3)] = 5
    cost[(1, 6)] = 1
    cost[(3, 1)] = 5
    cost[(3, 6)] = 6
    cost[(3, 4)] = 2
    cost[(2, 1)] = 4
    cost[(4, 2)] = 4
    cost[(4, 5)] = 3
    cost[(5, 2)] = 6
    cost[(5, 6)] = 3
    cost[(6, 4)] = 7
    # print(cost)
    # goal state
    goal = [6]

    # UCS
    answer = UCS(0, goal, graph, cost)
    print("UCS = ", answer[0])

    # BFS
    answer = BFS(0, goal, graph)
    print("BFS = ", answer[0])

    # DFS
    answer = DFS(0, goal, graph)
    print("DFS = ", answer[0])
