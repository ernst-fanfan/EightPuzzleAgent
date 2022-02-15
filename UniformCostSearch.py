
def UCS(start, goal, graph, cost):
    answer = []
    queue = []

    for i in range(len(goal)):
        answer.append(10 ** 8)

    queue.append([0, start])
    visited = {}
    count = 0

    while len(queue) > 0:
        queue = sorted(queue)
        p = queue[-1]
        del queue[-1]
        p[0] *= -1

        if p[1] in goal:
            index = goal.index(p[1])

            if answer[index] == 10 ** 8:
                count += 1

            if answer[index] > p[0]:
                answer[index] = p[0]

            del queue[-1]

            queue = sorted(queue)
            if count == len(goal):
                return [len(visited)]

        if p[1] not in visited:
            for i in range(len(graph[p[1]])):
                # value is multiplied by -1 so that
                # least priority is at the top
                queue.append([(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])

        visited[p[1]] = 1

    return [len(visited)]
