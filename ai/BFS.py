graph = {'S':['A','B'], 'A':['C','D'], 'B':['G','H'], 'C':['E','F'], 'D':[],
         'G':['I'], 'H':[], 'E':['K'], 'F':[], 'I':[], 'K':[]}
visited = [] #list of visited nodes
queue = [] #initialising the queue

#function for BFS
def bfs (visited, graph, node):
    visited.append(node)
    queue.append(node)
#creating loop to visit each node
    while queue:
        m = queue.pop(0)
        print(m, end = '')

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

#driver code
print("following is the breadth first search")
bfs(visited, graph, 'S')
