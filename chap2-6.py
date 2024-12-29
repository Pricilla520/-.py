class Node():
    def __init__(self,value=None):
        self.data=value
        self.next=None

class LinkQueue():
    def __init__(self):
        self.front=Node()
        self.rear=self.front
        self.capacity=10
        
    def length(self):
        if self.front==self.rear:
            return 0
        cursor=self.front
        count=0
        while cursor.next!=None:
            count=count+1
            cursor=cursor.next
        return count
    
    def en_queue(self,value):
        if self.length()==self.capacity:
            raise Exception('Full queue')
        node=Node(value)
        self.rear.next=node
        self.rear=node
        
    def de_queue(self):
        if self.front==self.rear:
            raise Exception("Empty queue!")
        top=self.front.next
        value=top.data
        self.front.next=top.next
        if self.rear==top:
            self.rear=self.front
        return value
    
    def traverse(self):
        if self.front==self.rear:
            raise Exception("Empty queue!")
        cursor=self.front.next
        while cursor!=None:
            print(cursor.data,end=' ')
            cursor=cursor.next