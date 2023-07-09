from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

from build.lib.Datastructures.linear.SLL import SLL

class StackLL(SLL):

    def __init__(self, head=None):
        super().__init__(head)

    def push(self, node):
        super().InsertHead(node)

    def pop(self):
        print(self.head.value)
        super().DeleteHead()
        

    def peek(self):
        if self.head is None:
            print("None")
        else:
            print(self.head.value)
    
    def size(self):
        print(self.size_list)
    
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
    
    def empty(self):
        if self.head is None:
            print("The stack is empty")
        else:
            print("The stack is not empty")

    def InsertTail(self, node):
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