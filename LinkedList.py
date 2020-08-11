class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head == None:
            return 'None'

        current = self.head
        llStr = current.data
        while current.next != None:
            current = current.next
            llStr = llStr + ", " + current.data
        return llStr



    def append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode

    def deleteWithValue(self, data):
        if self.head == None:
            return

        if self.head.data == data:
            self.head == self.head.next

        current = self.head

        while current.next != None:
            if current.next.data == data:
                current.next = current.next.next
            current = current.next
        
        

    def prepend(self, data):
        newNode = Node(data)
        
        newNode.next = self.head
        self.head = newNode

    def insert(self, atNode, data):
        if atNode is None:
            print("No at Node provided as input")
            return

        newNode = Node(data)

        newNode.next = atNode.next
        atNode.next = newNode


    # def getNext(self, next):
    #     return next

list1 = LinkedList()
print(list1)

list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.head.next = e2

# Link second Node to third node
e2.next = e3

print(list1.head.data)
print(list1.head.next.data)
print(list1.head.next.next.data)

print(list1)

list1.append("Thu")

print(list1)

list1.prepend("Sun")

print(list1)

list1.insert(list1.head.next , "Fri")

print(list1)

list1.deleteWithValue("Fri")

print(list1)






        

