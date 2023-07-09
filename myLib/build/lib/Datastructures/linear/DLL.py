from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

class DLL:
    size_list = 0

    def __init__(self, node=None):
        self.head = node
        self.tail = node

        if node is not None:
            self.size_list += 1

    def InsertHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size_list += 1

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = None
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size_list += 1

    def Insert(self, node, position):
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            i = 1
            while curr.next is not None:
                if i != (position - 1):
                    curr = curr.next
                elif i == (position - 1):
                    node.prev = curr
                    node.next = curr.next
                    curr.next = node
                    curr.next.prev = node
                    break
                i += 1
            if position == 1:
                self.InsertHead(node)
                return
            elif position <= 0 or position > self.size_list:
                print("Invalid Position")
                return
        self.size_list += 1

    def SortedInsert(self, node):
        if self.head is None:
            self.head = node
        else:
            is_sorted = True
            curr = self.head
            while curr.next is not None:
                if curr.next.value < node.value:
                    curr = curr.next
                else:
                    is_sorted = False
                    break
            if is_sorted:
                node.next = curr.next
                node.prev = curr
                if curr.next is not None:
                    curr.next.prev = node
                else:
                    self.tail = node
                curr.next = node
            else:
                self.Sort()
                curr = self.head
                while curr.next is not None and curr.next.value < node.value:
                    curr = curr.next
                if curr.next is None:
                    node.prev = curr
                    curr.next = node
                    self.tail = node
                else:
                    node.next = curr.next
                    node.prev = curr
                    curr.next = node
                    node.next.prev = node
        self.size_list += 1

    def Search(self, node): 
        curr = self.head
        while curr is not None and curr.next is not self.tail.next:
            if curr.value == node.value:
                print(curr)
                return
            curr = curr.next
        print(None)

    def DeleteHead(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size_list -= 1

    def DeleteTail(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size_list -= 1

    def Delete(self, node): 
        if self.head is None:
            return
        if self.head.value == node.value:
            node.next = self.head.next
            self.head = node.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            self.size_list -= 1
            return
        
        curr = self.head
        while curr.next is not None:
            if curr.value == node.value:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self.size_list -= 1
                return
            curr = curr.next

    def Sort(self):
        if self.head is None or self.head.next is None:
            return

        mov_curr = None
        curr = self.head
        while curr is not None:
            next_node = curr.next

            if mov_curr is None or curr.value < mov_curr.value:
                curr.next = mov_curr
                if mov_curr is not None:
                    mov_curr.prev = curr
                mov_curr = curr
            else:
                temp = mov_curr
                while temp.next is not None and temp.next.value < curr.value:
                    temp = temp.next
                curr.next = temp.next
                if temp.next is not None:
                    temp.next.prev = curr
                temp.next = curr
                curr.prev = temp
            curr = next_node

        self.head = mov_curr

        tailer = self.head
        while tailer.next is not None:
            tailer = tailer.next

        self.tail = tailer                   
       

    def Clear(self):
        self.head = None
        self.tail = None
        self.size_list = 0

    def Print(self):
        if self.head is None:
            print("The list is empty.")
            return

        is_sorted = True
        curr = self.head
        while curr.next is not None:
            if curr.value > curr.next.value:
                is_sorted = False
            curr = curr.next

        var_sort = ""
        if is_sorted:
            var_sort = "sorted"
        else:
            var_sort = "not sorted"
        print("The length of the list:", self.size_list)
        print("The list is", var_sort)
        curr = self.head
        print("The contents of the list are: ", end="")
        while curr is not None:
            print(curr.value, end=" <--> ")
            curr = curr.next
        print("None")
