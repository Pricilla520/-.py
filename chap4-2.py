G=[[0,2,99,99,5,7],
   [2,0,6,4,3,99],
   [99,6,0,8,7,99],
   [99,4,8,0,5,99],
   [5,3,7,5,0,9],
   [7,99,99,99,9,0]]

def Kruskal(G):
    nodenum=len(G)
    edgelist=[]
    result=[]
    for i in range(nodenum):
        for j in range(i,nodenum):
            if G[i][j]>0 and G[i][j]<99:
                edgelist.append([i,j,G[i][j]])
    edgelist.sort(key=lambda x:x[2])
    group=[]
    for i in range(nodenum):
        group.append([i])
    for edge in edgelist:
        for i in range(len(group)):
            if edge[0] in group[i]:
                start_group=i
            if edge[1] in group[i]:
                end_group=i
        if start_group!=end_group:
            result.append(edge)
            group[start_group]=group[start_group]\
                +group[end_group]
            group[end_group]=[]
    return result
    

print(Kruskal(G))