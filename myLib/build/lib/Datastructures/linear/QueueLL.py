from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

from build.lib.Datastructures.linear.SLL import SLL

class QueueLL(SLL):
    def __init__(self, head=None):
        super().__init__(head)

    def enqueue(self, node):
        super().InsertTail(node)
    
    def dequeue(self):
        super().DeleteHead()

    def front(self):
        if self.head is None:
            return None
        else:
            return self.head
    
    def empty(self):
        if self.head is None:
            print("The queue is empty")
        else:
            print("The queue is not empty")
    
    def peek(self):
        if self.head is None:
            print("None")
        else:
            print(self.head.value)
    
    def size(self):
        print(self.size_list)
        return
    
    def Search(self, node):
        curr = self.head
        counter = 1
        while curr is not None:
            if curr.value == node.value:
                print(counter)
                return
            curr = curr.next
            counter +=1
        print(-1)
        return
    
    def InsertHead(self, node):
        pass
    
    def Insert(self, node, position):
        pass
    
    def SortedInsert(self, node):
        pass

    def DeleteTail(self):
        pass

    def Delete(self, node):
        pass

    def Sort(self):
        pass

