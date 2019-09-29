from collections import namedtuple
# import pdb; pdb.set_trace()

pair = namedtuple("pair", ["first", "second"])

class  graph:
    def __init__(self):
        self.matrix = []
        self.vertexCount = 0

    def clear(self):
        self.__init__()

    def add(self, edge1, edge2, val):
        edge1 = int(edge1) - 1
        edge2 = int(edge2) - 1
        val = int(val)
        if edge1 >= self.vertexCount:
            for i in range(edge1 - self.vertexCount + 1):
                self.matrix.append([])
            # self.matrix.append([] * (edge1 - self.vertexCount + 1))
            self.vertexCount = len(self.matrix)
        if edge2 >= self.vertexCount:
            for i in range(edge2 - self.vertexCount + 1):
                self.matrix.append([])
            self.vertexCount = len(self.matrix)
        self.matrix[edge1].append(pair(edge2, val))
        self.matrix[edge2].append(pair(edge1, val))

    def deWay(self, s):
        distance = [10000] * self.vertexCount
        # parent = [0] * self.vertexCount
        used = [0] * self.vertexCount
        distance[s] = 0
        for i in range(self.vertexCount):
            v = -1
            for j in range(self.vertexCount):
                if used[j] == 0 and (v == -1 or distance[j] < distance[v]):
                    v = j
            if distance[v] == 10000:
                print(-1)
                break;
            used[v] = 1

            for j in range(len(self.matrix[v])):
                next = self.matrix[v][j].first
                size = self.matrix[v][j].second
                if distance[v] + size < distance[next]:
                    distance[next] = distance[v] + size
                    # print(next)
                    # parent[next] = v
        # print(max(distance))
        max = 0
        for i in range(len(distance)):
            if max < distance[i]:
                max = distance[i]
        print(max)


gr = graph()
n = int(input())
s = input().split()
for i in range(0, len(s), 3):
    gr.add(s[i], s[i + 1], s[i + 2])
s = int(input())
gr.deWay(s)
