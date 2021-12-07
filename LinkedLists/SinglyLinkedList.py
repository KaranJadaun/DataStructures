class Node:
    def __init__(self):
        self.info = None
        self.next = None

class Linkedlist:
    def __init__(self):
        self.start = None

    def create(self):
        while(1):
            node = Node()
            node.info = input("enter info: ")
            if (self.start is None):
                self.start = node
            else:
                temp.next = node
            temp = node
            ch = input("do you want to add more nodes(y/n): ")
            if (ch=='n'):
                print("linkedlist created successfully")
                break

    def display(self):
        temp = self.start
        if (self.start is None):
            print("No linkedlist exist!")
            return
        while(temp.next is not None):
            print(temp.info, "->", end=" ")
            temp = temp.next
        print(temp.info)

    def insert_at_beg(self):
        node = Node()
        node.info = input("enter info: ")
        if (self.start is None):
            self.start = node
            return
        node.next = self.start
        self.start = node

    def insert_at_end(self):
        node = Node()
        node.info = input("enter info: ")
        if (self.start is None):
            self.start = node
            return
        temp = self.start
        while(temp.next is not None):
            temp = temp.next
        temp.next = node

    def insert_after_given_node(self):
        value = input("enter given value: ")
        temp = self.start
        while(temp.info != value):
            temp = temp.next
        if (temp is None):
            print("value not found")
            return
        node = Node()
        node.info = input("enter info: ")
        node.next = temp.next
        temp.next = node
    
    def delete_from_beg(self):
        if (self.start is None):
            print("no linkedlist exist")
            return
        self.start = self.start.next

    def delete_from_end(self):
        if (self.start is None):
            print("no linkedlist exist")
            return
        temp = self.start
        while (temp.next is not None):
            temp = temp.next
        temp.next = None

    def delete_after_given_node(self):
        value = input("enter value: ")
        temp = self.start
        while(temp.info != value):
            temp = temp.next
        if (temp.next is None):
            print("no linkedlist exist")
            return
        temp.next = temp.next.next
        


sll = Linkedlist()
while(1):
    print("what do you want to do?")
    print("press 1 to create")
    print("press 2 to display")
    print("press 3 to insert at beginning")
    print("press 4 to insert at end")
    print("press 5 to insert after given node")
    print("press 100 to quit")
    operation = int(input("enter operation: "))
    if (operation==1):
        sll.create()
    if (operation==2):
        sll.display()
    if (operation==3):
        sll.insert_at_beg()
    if (operation==4):
        sll.insert_at_end()
    if (operation==5):
        sll.insert_after_given_node()
    if (operation==100):
        break
