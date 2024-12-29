class Stack():
    def __init__(self):
        self.elem=[]
    def is_empty(self):
        return len(self.elem)==0
    def push(self,x):
        self.elem.append(x)
    def pop(self):
        return self.elem.pop()
    def top(self):
        return self.elem[len(self.elem)-1]
    def length(self):
        return len(self.elem)
    def traverse(self):
        print(self.elem)

# def shi_to_shiliu(n):
#     stack=Stack()
#     lst=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
#     while n!=0:
#         r=n%16
#         stack.push(lst[r])
#         n=n//16
#     s=''
#     while not stack.is_empty():
#         s=s+str(stack.pop())
#     return s
# print(shi_to_shiliu(1100))

def match(expr):
    stack=Stack()
    for ch in expr:
        if ch in ['(','[','{']:
            stack.push(ch)
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