class Node:
    def __init__(self):
        self.info = None
        self.prev = None
        self.next = None

class Linkedlist:
    def __init__(self):
        self.start = None

    def create(self):
        while(1):
            node = Node()
            node.info = input("Enter Info : ")
            if (self.start is None):
                self.start = node
            else:
                temp = self.start
                while(temp.next is not None):
                    temp = temp.next
                temp.next = node
                node.prev = temp
            ch = input("Do you want to insert more node: (y/n) : ")
            if (ch=='n'):
                break

    def display(self):
        if (self.start is None):
            print("No LinkedList Exist")
            return
        temp = self.start
        while(temp.next is not None):
            print(temp.info,end=" -> ")
            temp = temp.next
        print(temp.info)
    
    def insert_at_began(self):
        if (self.start is None):
            print("No LinkedList Exists")
            return
        node = Node()
        node.info = input("Enter Info : ")
        node.next = self.start
        self.start.prev = node
        self.start = node

    def insert_at_end(self):
        if (self.start is None):
            print("No LinkedList Exists")
            return
        node = Node()
        node.info = input("Enter Info : ")
        temp = self.start 
        while(temp.next is not None):
            temp = temp.next
        temp.next = node
        node.prev = temp

    def insert_after_given_value(self):
        if (self.start is None):
            print("No LinkedList Exists")
            return
        val = input("Enter value to insert after : ") 
        node = Node()
        node.info = input("Enter Info : ")
        temp = self.start
        while(val!=temp.info and temp.next is not None):
            temp = temp.next
        if (temp.next is None):
            print("Value not found")
            return
        node.prev = temp
        node.next = temp.next
        temp.next = node
        node.next.prev = node

    def delete_from_began(self):
        if (self.start is None):
            print("No LinkedList Exists")
            return
        self.start = self.start.next
        self.start.prev = None
    
    def delete_from_end(self):
        if (self.start is None):
            print("No LinkedList Exists")
            return
        temp = self.start
        while(temp.next is not None):
            temp = temp.next
        temp.prev.next = None
    
    def delete_value(self):
        if (self.start is None):
            print("No LinkedList Exists")
            return
        val = input("Enter Value to be deleted : ")
        temp = self.start 
        while(val!=temp.info and temp.next is not None):
            temp = temp.next
        if (temp.next is None):
            print("Value not found")
            return
        temp.prev.next = temp.next 
        temp.next.prev = temp.prev

    def delete_linkedlist(self):
        self.start = None
    

dll = Linkedlist()
while(1):
    print("1.Create")
    print("2.Display")
    print("3.Insert at Began")
    print("4.Insert at End")
    print("5.Insert after given value")
    print("6.Delete from Began")
    print("7.Delete from End")
    print("8.Delete Value")
    print("9.Delete LinkedList")
    print("100.Quit")
    op = int(input("Enter Operation : "))
    if (op==1):
        dll.create()
    if (op==2):
        dll.display()
    if (op==3):
        dll.insert_at_began()
    if (op==4):
        dll.insert_at_end()
    if (op==5):
        dll.insert_after_given_value()
    if (op==6):
        dll.delete_from_began()
    if (op==7):
        dll.delete_from_end()
    if (op==8):
        dll.delete_value()
    if (op==9):
        dll.delete_linkedlist()
    if (op==100):
        break
