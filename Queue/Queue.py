class Queue:
    def __init__(self):
        self.rear = -1
        self.front = -1
        self.size = 10
        self.q = [None for i in range(self.size)]

    def enqueue(self):
        if (self.rear == (self.size-1)):
            print("Queue Overflow")
            return
        value = input("Enter Info : ")
        self.rear += 1
        self.q[self.rear] = value
        if (self.front == -1):
            self.front = 0

    def dequeue(self):
        if (self.front == -1):
            print("Queue Underflow")
            return
        for i in range(self.rear):
            self.q[i] = self.q[i+1]
        self.rear -= 1

    def display(self):
        for i in range(self.front,self.rear+1):
            print(self.q[i])

q = Queue()
while(1):
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("100.Quit")
    op = int(input("Enter Operation : "))
    if (op==1):
        q.enqueue()
    if (op==2):
        q.dequeue()
    if (op==3):
        q.display()
    if (op==100):
        break
