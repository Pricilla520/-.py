class Node():
    def __init__(self,value=None):
        self.data=value
        self.next=None

class LinkList():
    def __init__(self,node=None):
        self.head=node
    def append(self,node=None):
        if self.head==None:
            self.head=node
        else:
            cursor=self.head
            while cursor.next!=None:
                cursor=cursor.next
            cursor.next=node
    def length(self):
        if self.head==None:
            return 0
        else:
            cursor=self.head
            count=1
            while cursor.next!=None:
                cursor=cursor.next
                count=count+1
            return count
                    
    def insert(self,pos,node):
        if pos>self.length():
            self.append(node)
        elif pos<-self.length() or pos==0:
            node.next=self.head
            self.head=node
        else:
            if pos<0:
                pos=self.length()+pos+2
            cursor=self.head
            count=1
            while count<pos-1:
                cursor=cursor.next
                count=count+1
            node.next=cursor.next
            cursor.next=node
    def traverse(self):
        if self.head==None:
            raise Exception("Empty list!")
        else:
            cursor=self.head
            while cursor.next!=None:
                print(cursor.data,end=' ')
                cursor=cursor.next
            print(cursor.data)
    def remove(self,x):
        if self.head==None:
            raise Exception("Empty list!")
        else:
            while self.head!=None and self.head.data==x:
                self.head=self.head.next
            cursor=self.head
            if self.head!=None:
                while cursor.next!=None:
                    if cursor.next.data==x:
                        cursor.next=cursor.next.next
                    else:
                        cursor=cursor.next
    def delete(self,pos):
        if pos>self.length():
            pos=self.length()
        if pos<1:
            pos=1
        cursor=self.head
        count=1
        if pos==1:
            self.head=self.head.next
        else:
            while count<pos-1:
                cursor=cursor.next
                count=count+1
            cursor.next=cursor.next.next
        
                
llist=LinkList()
llist.head=Node(1)
for i in range(9):
    llist.append(Node(i+2))
llist.traverse()
print('\n')
llist.delete(5)
llist.traverse()