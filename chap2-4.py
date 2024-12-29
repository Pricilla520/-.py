class Queue():
    def __init__(self,n=8):
        self.capacity=n
        self.elem=[None]*n
        self.front=0
        self.rear=0
    def is_empty(self):
        return self.front==self.rear
    def is_full(self):
        return (self.rear+1)%self.capacity==self.front
    def en_queue(self,x):
        if self.is_full():
            raise Exception("Full queue!")
        if self.is_empty():
            self.elem.append(x)
            self.rear=(self.rear+1)%self.capacity
            return
        self.elem[self.rear]=x
        self.rear=(self.rear+1)%self.capacity
    def de_queue(self):
        if self.is_empty():
            raise Exception("Empty queue!")
        self.front=self.front+1
    def length(self):
        return (self.rear-self.front+self.capacity)%self.capapcity
                            
queue=Queue()
for i in range(9):
    queue.en_queue(i)
    print(queue.front)
    print(queue.rear)