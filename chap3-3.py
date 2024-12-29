def Freq(string):
    freq={}
    for ch in string:
        if ch not in freq:
            freq[ch]=1
        else:
            freq[ch]=freq[ch]+1
    lst=sorted(freq.items(),key=lambda x:x[1])
    queue=[]
    for i in lst:
        queue.append(Node(i))
    return queue
        
class Node():
    def __init__(self,data):
        self.lchild=None
        self.rchild=None
        self.value=data[0]
        self.priority=data[1]
        self.code=''

def AddNode(queue,node):
    if len(queue)==0:
        return [node]
    else:
        for i in range(len(queue)):
            if queue[i].priority>=node.priority:
                queue=queue[:i]+[node]+queue[i:]
                return queue
    queue.append(node)
    return queue
        
def CreateHTree(queue):
    while len(queue)!=1:
        node1=queue.pop(0)
        node2=queue.pop(0)
        new_node=Node([None,node1.priority+\
                       node2.priority])
        new_node.lchild=node1
        new_node.rchild=node2
        queue=AddNode(queue,new_node)
    return queue.pop(0)

Encoder={}  
Decoder={}    
def Tree2Code(root,x):
    if root==None:
        pass
    else:
        if root.value!=None:
            Encoder[root.value]=root.code+x
            Decoder[root.code+x]=root.value
        Tree2Code(root.lchild,x+'0')
        Tree2Code(root.rchild,x+'1')

def Encode(string):
    result=''
    for ch in string:
        result=result+Encoder[ch]
    return result

def Decode(string):
    result=''
    temp=''
    for ch in string:
        temp=temp+ch
        if temp in Decoder:
            result=result+Decoder[temp]
            temp=''
    return result

s='bbaddccccddeeeffffffgaabbcccdeefefefffabcdef'
queue=Freq(s)
root=CreateHTree(queue)
Tree2Code(root,'')
a=Encode(s)
b=Decode(a)
print(Encoder)
print(Decoder)
print(a)
print(b)
print(b==s)
