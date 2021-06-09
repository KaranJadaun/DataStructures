# Like arrays, Linked List is a linear data structure. 
# Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers.

# Creating a class node so that we can assign data to the linkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# This class contains a Node object    
class Linkedlist:
    
    # Funtion to assign head
    def __init__(self):
        self.head = None
        
    # Fucntion for printing Linkedlist
    # We can also use str mehtod but it was bit complicated
    def printLinkedlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
Linked = Linkedlist()
Linked.head = Node(11)
linked2 = Node(22)
linked3 = Node(33)
Linked.head.next = linked2
linked2.next = linked3
Linked.printLinkedlist()
