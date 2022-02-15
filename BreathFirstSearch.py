def BFS(start, goal, graph):
    queue = []
    visited = {}

    queue.append(start)
    visited[start] = True

    while queue:
        s = queue.pop(0)

        for i in graph[s]:
            if goal[0] == i:
                return [len(visited) - 1]
            if not visited.get(i, False):
                queue.append(i)
                visited[i] = True

    return [len(visited) - 1]
