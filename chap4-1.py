class Vertex():
    def __init__(self,name):
        self.name=name
        self.link=[]

class Graph():
    def __init__(self,vertexes=[]):
        self.vertex_list={}
        for x in vertexes:
            self.vertex_list[x]=[]
    def AddEdge(self,start,end):
        if start not in self.vertex_list:
            raise Exception('No vertex: ',start)
        if end not in self.vertex_list:
            raise Exception('No vertex: ',end)
        if end in self.vertex_list[start]:
            return
        self.vertex_list[start].append(end)
        self.vertex_list[end].append(start)
    def RemoveEdge(self,start,end):
        if start not in self.vertex_list:
            raise Exception('No vertex: ',start)
        if end not in self.vertex_list:
            raise Exception('No vertex: ',end)
        if end not in self.vertex_list[start]:
            return
        self.vertex_list[start].remove(end)
        self.vertex_list[end].remove(start)
    def AddVertex(self,name):
        if name in self.vertex_list:
            raise Exception('Already exist')
        self.vertex_list[name]=[]
    def RemoveVertex(self,name):
        if name not in self.vertex_list:
            raise Exception('Vertex not exist')
        self.vertex_list.pop(name)
        for vertex in self.vertex_list:
            if name in self.vertex_list[vertex]:
                self.vertex_list[vertex].remove(name)

def DFS(G,start):
    lst=[start]
    visited=[]
    while lst:
        x=lst.pop()
        if x not in visited:
            print(x,end=' ')
            visited.append(x)
            lst.extend(G.vertex_list[x])

def BFS(G,start):
    lst=[start]
    visited=[]
    while lst:
        x=lst.pop(0)
        if x not in visited:
            print(x,end=' ')
            visited.append(x)
            lst.extend(G.vertex_list[x])
        
G=Graph([1,2,3,4,5,6,7])
G.AddEdge(1,5)
G.AddEdge(2,3)
G.AddEdge(3,4)
G.AddEdge(2,4)
G.AddEdge(1,2)
G.AddEdge(3,5)
G.AddEdge(5,6)
G.AddEdge(3,7)
G.AddEdge(6,7)
BFS(G,1)
