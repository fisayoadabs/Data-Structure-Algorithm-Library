from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

from build.lib.Datastructures.linear.SLL import SLL

class CSLL(SLL):

    def __init__(self, node=None):
        super().__init__(node)
        if node is not None:
            node.next = node
            self.tail = node

    def InsertHead(self, node):
        if self.head is None:
            self.head = node
            node.next = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        self.size_list += 1

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            node.next = node
            self.tail = node
        else:
            node.next = self.head
            self.tail.next = node
            self.tail = node
        self.size_list += 1

    def DeleteHead(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size_list -= 1

    def DeleteTail(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next
            curr.next = self.head
            self.tail = curr
        self.size_list -= 1

    def Sort(self):
        if self.head is None or self.head.next == self.head:
            return


        for i in range(self.size_list - 1):
            current = self.head
            for j in range(self.size_list - i - 1):
                if current.value > current.next.value:
                    temp = current.value
                    current.value = current.next.value
                    current.next.value = temp
                current = current.next
        self.UpdateTail()
    
    def Clear(self):
        super().Clear()

    def Print(self):
        if self.head is None:
            print("The list is empty")
        else:
            print("Size of list: ", self.size_list)
            curr = self.head
            is_sorted = True
            if self.head is not None:
                curr = self.head
                while curr.next is not self.head:
                    if curr.value > curr.next.value:
                        is_sorted = False
                    curr = curr.next
                if self.tail.value < self.head.value:
                    is_sorted = False
            else:
                is_sorted = False
            var_sort = ""
            if is_sorted is True:
                var_sort += "sorted"
            else:
                var_sort += "not sorted"
            print("The list is", var_sort)
            curr = self.head
            print("The contents of the list are: ", end="")
            while curr.next != self.head:
                print(curr.value, end=" -> ")
                curr = curr.next
            print(curr.value)
