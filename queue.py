class QueueList:
    def _init_(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,items):
        self.items.append(items)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from an empty queue")
            
    def size(self):
        return len(self.items)
    
queue=QueueList()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("front of the queue:",queue.peek())
print("Dequeue:",queue.dequeue())
print("Size of the queue",queue.size())