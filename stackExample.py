class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None

class Stack:

    def __init__(self):
        self.top = None

    def __str__(self):
        if self.top == None:
            return 'None'

        current = self.top
        llStr = current.data
        while current.prev != None:
            current = current.prev
            llStr = llStr + ", " + current.data
        return llStr



    def pop(self):
        data = self.top.data
        self.top = self.top.prev
        return data

    def peek(self):
        return self.top.data

    
    def push(self, data):
        newNode = Node(data)

        if self.top == None:
            self.top = newNode
            return

        newNode.prev = self.top
        self.top = newNode

AStack = Stack()
AStack.push("Mon")
AStack.push("Tue")
AStack.peek()
print(AStack.peek())

AStack.push("Wed")
AStack.push("Thu")
print(AStack.peek())

AStack1 = Stack()
AStack1.push("Mon")
AStack1.push("Tue")
AStack1.push("Wed")
AStack1.push("Thu")
print(AStack1.pop())
print(AStack1.pop())
        


        
    