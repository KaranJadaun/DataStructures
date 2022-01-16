class Stack:
    def __init__(self):
        self.top = -1
        self.size = 10
        self.st = [None for i in range(self.size)]

    def display(self):
        for i in range(0,self.top+1):
            print(self.st[i])

    def push(self):
        if (self.top == (self.size-1)):
            print("Stack Overflow")
            return
        value = input("Enter Info : ")
        self.top += 1
        self.st[self.top] = value

    def pop(self):
        if (self.top == -1):
            print("Stack Underflow")
            return
        self.top -= 1 

st = Stack()
while(1):
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("100.Quit")
    op = int(input("Enter Operation : "))
    if (op==1):
        st.push()
    if (op==2):
        st.pop()
    if (op==3):
        st.display()
    if (op==100):
        break
