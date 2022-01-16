class Node:
    def __init__(self):
        self.info = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def inorder(root):
        if (root is None):
            print("No Tree Exists")
            return
        Tree.inorder(root.left)
        print(root.info)
        Tree.inorder(root.right)

    def preorder(root):
        if (root is None):
            print("No Tree Exists")
            return
        print(root.info)
        Tree.preorder(root.left)
        Tree.preorder(root.right)

    def postorder(root):
        if (root is None):
            print("No Tree Exists")
            return
        Tree.postorder(root.left)
        Tree.postorder(root.right)
        print(root.info)

    def insertion(self):
        node = Node()
        node.info = input("Enter Info : ")
        if (self.root is None):
            self.root = node
            return
        temp = self.root
        while (temp is not None):
            par = temp
            if (temp.info>node.info):
                temp = temp.left
            else:
                temp = temp.right
        if (node.info<par.info):
            par.left = node
        else:
            par.right = node


t = Tree()
while(1):
    print("1.Insertion")
    print("2.Inorder Display")
    print("100.Quit")
    op = int(input("Enter Operation : "))
    if (op==1):
        t.insertion()
    if (op==2):
        t.inorder()
    if (op==100):
        break
