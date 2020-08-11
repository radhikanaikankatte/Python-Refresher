class Queue:

    def __init__(self):
        self.queue = []

    def pop(self):
        data = self.top.data
        self.top = self.top.prev
        return data

    def peek(self):
        return self.queue[-1]

    def size(self):
      return len(self.queue)

    
    def add(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        
        return False

    def remove(self):
        return self.queue.pop()


TheQueue = Queue()
TheQueue.add("Mon")
TheQueue.add("Tue")
TheQueue.add("Wed")
print(TheQueue.remove())
print(TheQueue.remove())