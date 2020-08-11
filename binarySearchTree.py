class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def insert(self, value):
        if self.data is None:
            self.data = value
            return

        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if self.data == value:
            return str(value) + " is found"
        elif value < self.data:
            if self.left is None:
                return str(value) + " not found"
            else:
                return self.left.find(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + " not found"
            else:
                return self.right.find(value)




# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()

print(root.find(7))
print(root.find(14))