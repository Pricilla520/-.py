class TreeNode:
    def __init__(self,value=None,lchild=None,rchild=None):
        self.data=value
        self.lchild=lchild
        self.rchild=rchild

class BinaryTree:
    def __init__(self,root=None):
        self.root=root
    def Traverse(self):
        lst=[]
        if self.root==None:
            raise Exception('Empty tree')
        else:
            queue=[self.root]
            while queue:
                elem=queue.pop(0)
                lst.append(elem.data)
                if elem.lchild!=None:
                    queue.append(elem.lchild)
                if elem.rchild!=None:
                    queue.append(elem.rchild)
        print(lst)
        
    def PreOrder(self,root):
        if root==None:
            return
        print(root.data,end=' ')
        self.PreOrder(root.lchild)
        self.PreOrder(root.rchild)
        
    def InOrder(self,root):
        if root==None:
            return
        self.InOrder(root.lchild)
        print(root.data,end=' ')
        self.InOrder(root.rchild)
        
    def PostOrder(self,root):
        if root==None:
            return
        self.PostOrder(root.lchild)
        self.PostOrder(root.rchild)
        print(root.data,end=' ')
        
node4=TreeNode(4,None,TreeNode(7))
node5=TreeNode(5,TreeNode(8),TreeNode(9))
node2=TreeNode(2,node4,node5)
node3=TreeNode(3,None,TreeNode(6))
node1=TreeNode(1,node2,node3)
bt=BinaryTree(node1)
bt.PreOrder(bt.root)
print('\n')
bt.InOrder(bt.root)
print('\n')
bt.PostOrder(bt.root)
print('\n')
bt.Traverse()