class Node():
    def __init__(self,value=None):
        self.data=value
        self.next=None

class LinkStack():
    def __init__(self,node=None):
        self.top=node
    def is_empty(self):
        return self.top==None
    def push(self,node=None):
        if self.top==None:
            self.top=node
        else:
            node.next=self.top
            self.top=node
    def pop(self):
        if self.top==None:
            raise Exception('Empty stack!')
        e=self.top.data
        self.top=self.top.next
        return e

def shi_to_shiliu(n):
    stack=LinkStack()
    lst=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    while n!=0:
        r=n%16
        stack.push(Node(lst[r]))
        n=n//16
    s=''
    while not stack.is_empty():
        s=s+str(stack.pop())
    return s
print(shi_to_shiliu(1100))

def match(expr):
    stack=LinkStack()
    for ch in expr:
        if ch in ['(','[','{']:
            stack.push(Node(ch))
        if ch==')':
            x=stack.pop()
            if x=='(':
                pass
            else:
                return False
        if ch==']':
            x=stack.pop()
            if x=='[':
                pass
            else:
                return False
        if ch=='}':
            x=stack.pop()
            if x=='{':
                pass
            else:
                return False
    return stack.is_empty()
print(match('3+5*[3+5{4-2(sadf[ghfh]fghgf)hfhg}]'))