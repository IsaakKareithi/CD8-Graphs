def dfs(graph, start):

    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                stack.append(neighbour)
        return visited   


graph = {
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : [],
    'E' : [] 
}

visited = dfs(graph, 'A')

print(visited)