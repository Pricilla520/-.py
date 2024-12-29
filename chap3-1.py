class TreeNode:
    def __init__(self,value=None,lchild=None,rchild=None):
        self.data=value
        self.lchild=lchild
        self.rchild=rchild

class CompleteTree:
    def __init__(self,root=None):
        self.root=root
    
    def AddNode(self,node=None):
        if self.root==None:
            self.root=node
        else:
            queue=[self.root]
            while queue:
                elem=queue.pop(0)
                if elem.lchild==None:
                    elem.lchild=node
                    return
                if elem.rchild==None:
                    elem.rchild=node
                    return
                queue.append(elem.lchild)
                queue.append(elem.rchild)

node2=TreeNode(2)
node3=TreeNode(3)
node1=TreeNode(1,node2,node3)
bt=CompleteTree(node1)
for i in range(4,12):
    bt.AddNode(TreeNode(i))

print(bt.root.lchild.rchild.lchild.data)