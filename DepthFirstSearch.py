def DFSUtil(v, goal, visited, graph):
    visited.append(v)

    for neighbour in graph[v]:
        if neighbour not in visited:
            if visited[-1] == goal[0]:
                return len(visited) - 1

            DFSUtil(neighbour, goal, visited, graph)

    return len(visited) - 1


def DFS(start, goal, graph):
    visited = []
    return [DFSUtil(start, goal, visited, graph)]
