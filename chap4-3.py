G=[[0,2,99,99,5,7],
   [2,0,6,4,3,99],
   [99,6,0,8,7,99],
   [99,4,8,0,5,99],
   [5,3,7,5,0,9],
   [7,99,99,99,9,0]]

def Prim(G):
    nodenum=len(G)
    result=[]
    visited=[0]
    unvisited=[i for i in range(1,nodenum)]
    while len(unvisited)>0:
        min_distance=99
        for i in visited:
            for j in unvisited:
                if G[i][j]<min_distance:
                    min_distance=G[i][j]
                    start,end=i,j
        visited.append(end)
        unvisited.remove(end)
        result.append([start,end,G[start][end]])
    return result

print(Prim(G))