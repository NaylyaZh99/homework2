# import pdb; pdb.set_trace()
class  graph:
    def __init__(self):
        self.matrix = []
        self.vertexCount = 0

    def clear(self):
        self.__init__()

    def add(self, edge1, edge2):
        edge1 = int(edge1)
        edge2 = int(edge2)
        if edge1 >= self.vertexCount:
            for i in range(edge2 - self.vertexCount + 1):
                self.matrix.append([])
            # self.matrix.append([] * (edge1 - self.vertexCount + 1))
            self.vertexCount = len(self.matrix)
        if edge2 >= self.vertexCount:
            for i in range(edge2 - self.vertexCount + 1):
                self.matrix.append([])
            self.vertexCount = len(self.matrix)
        self.matrix[edge1].append(edge2)
        self.matrix[edge2].append(edge1)

    def dfs(self, v, used):
        used[v] = 1
        print(v)
        for i in range(len(self.matrix[v])):
            next = self.matrix[v][i]
            if used[next] == 0:
                self.dfs(next, used)
        return

    def bfs(self, v):
        queue = []
        queue.append(v)
        used = [0] * gr.vertexCount
        used[v] = 1
        while len(queue) != 0:
            v = queue.pop(0)
            print(v)
            for i in range(len(self.matrix[v])):
                next = self.matrix[v][i]
                if used[next] == 0:
                    used[next] = 1
                    queue.append(next)


gr = graph()
s = input().split()
for i in range(0, len(s), 2):
    gr.add(s[i], s[i + 1])
# print(gr.matrix)
used = [0] * gr.vertexCount
# print(used)
# gr.dfs(0, used)
gr.bfs(0)
