class Node:
    def __init__(self):
        self.info = None
        self.next = None

class LinkedList:
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
                while (temp.next is not None):
                    temp = temp.next
                temp.next = node
            ch = input("Do you want to insert more node: (y/n) : ")
            if (ch=='n'):
                break

    def display(self):
        if (self.start is None):
            print("No LinkedList Exists")
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
        node.next = temp.next
        temp.next = node

    def delete_from_began(self):
        if (self.start is None):
            print("No LinkedList Exists")
            return
        self.start = self.start.next

    def delete_from_end(self):
        if (self.start is None):
            print("No LinkedList Exists")
            return
        temp = self.start
        prev = None
        while(temp.next is not None):
            prev = temp
            temp = temp.next
        prev.next = None   

    def delete_value(self):
        if (self.start is None):
            print("No LinkedList Exists")
            return
        val = input("Enter Value to be deleted : ")
        temp = self.start 
        while(val!=temp.info and temp.next is not None):
            prev = temp
            temp = temp.next
        if (temp.next is None):
            print("Value not found")
            return
        prev.next = temp.next    

    def delete_linkedlist(self):
        self.start = None

    def length_of_linkedlist(self):
        temp = self.start
        count = 0
        while (temp is not None):
            count += 1
            temp = temp.next
        print(count)
        return

    def search(self):
        value = input("Enter Value to be searched : ")
        temp = self.start
        while (value!=temp.info and temp is not None):
            temp = temp.next
        if (temp is None):
            print("Value not found")
        else:
            print("Value found")

    def get_nth_node(self):
        nth = int(input("Enter nth node : "))
        temp = self.start
        while (nth!=1 and temp is not None):
            nth -= 1
            temp = temp.next
        if  (temp is None):
            print("Node is out of bound")
        else:
            print(temp.info)

    def get_nth_node_from_end(self):
        nth = int(input("Enter nth node from end : "))
        temp = self.start
        count = 0
        while (temp is not None):
            count += 1
            temp = temp.next
        lth = count - nth + 1
        temp1 = self.start
        while(lth!=1 and temp1 is not None):
            lth -= 1
            temp1 = temp1.next
        if  (temp1 is None):
            print("Node is out of bound")
        else:
            print(temp1.info)

    def get_middle_of_linkedlist(self):
        slow = fast = self.start
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        print(slow.info)
        return

    def count_no_of_occurances(self):
        num = input("Enter Element : ")
        temp = self.start
        count = 0
        while (temp is not None):
            if (temp.info == num):
                count += 1
            temp = temp.next
        print(count)
        return


sll = LinkedList()
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
    print("10.Number of nodes")
    print("11.Searching Element")
    print("12.Get nth node")
    print("13.Get nth node from end")
    print("14.Get middle of the linkedlist")
    print("15.Get number of occurances")
    print("100.Quit")
    op = int(input("Enter Operation : "))
    if (op==1):
        sll.create()
    if (op==2):
        sll.display()
    if (op==3):
        sll.insert_at_began()
    if (op==4):
        sll.insert_at_end()
    if (op==5):
        sll.insert_after_given_value()
    if (op==6):
        sll.delete_from_began()
    if (op==7):
        sll.delete_from_end()
    if (op==8):
        sll.delete_value()
    if (op==9):
        sll.delete_linkedlist()
    if (op==10):
        sll.length_of_linkedlist()
    if (op==11):
        sll.search()
    if (op==12):
        sll.get_nth_node()
    if (op==13):
        sll.get_nth_node_from_end()
    if (op==14):
        sll.get_middle_of_linkedlist()
    if (op==15):
        sll.count_no_of_occurances()
    if (op==100):
        break
