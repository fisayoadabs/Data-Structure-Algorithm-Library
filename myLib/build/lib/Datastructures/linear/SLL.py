from pathlib import Path
import sys

path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))


class SLL:
    size_list = 0

    def __init__(self, head=None):
        self.head = head
        if head is not None:
            self.size_list += 1
        self.UpdateTail()

    def InsertHead(self, node):
        node.next = self.head
        self.head = node
        self.size_list += 1
        self.UpdateTail()

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
        self.size_list += 1
        self.UpdateTail()

    def Insert(self, node, position):
        if position <= 0 or position > self.size_list + 1:
            print("Invalid position")
            return
        elif position == 1:
            self.InsertHead(node)
        elif position == self.size_list + 1:
            self.InsertTail(node)
        else:
            curr = self.head
            i = 1
            while i < (position - 1):
                curr = curr.next
                i += 1
            node.next = curr.next
            curr.next = node
            self.size_list += 1
        self.UpdateTail()


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
                curr.next = node
            else:
                self.Sort()
                present = None
                curr = self.head
                while curr is not None and curr.value < node.value:
                    present = curr
                    curr = curr.next
                node.next = curr
                if present is not None:
                    present.next = node
                else:
                    self.head = node
        self.size_list += 1
        self.UpdateTail()

    def Search(self, node): 
        curr = self.head
        while curr is not None:
            if curr.value == node.value:
                print(curr)
                return
            curr = curr.next
        print(None)

    def DeleteHead(self):
        if self.head is None:
            return
        else:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size_list -= 1
            self.UpdateTail()

    def DeleteTail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None
        self.size_list -= 1
        self.UpdateTail()

    def Delete(self, node):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        if node is None:
            return
        if self.head.next.value == node.value:
            self.head.next = self.head.next.next
            self.size_list -= 1
            self.UpdateTail()
            return
        else:
            curr = self.head
            while curr.next is not None:
                if curr.next.value == node.value:
                    curr.next = curr.next.next
                    self.size_list -= 1
                    self.UpdateTail()
                    return
                curr = curr.next
        self.size_list -= 1

    def Sort(self):
        if self.head is None or self.head.next is None:
            return

        first_check = self.head
        second_check = self.head.next
        first_check.next = None

        while second_check is not None:
            curr = second_check
            second_check = second_check.next
            if curr.value <= first_check.value:
                curr.next = first_check
                first_check = curr
            else:
                moving_curr = first_check
                while (
                    moving_curr.next is not None and moving_curr.next.value < curr.value
                ):
                    moving_curr = moving_curr.next
                curr.next = moving_curr.next
                moving_curr.next = curr
        self.head = first_check
        self.UpdateTail()

    def Clear(self):
        self.head = None
        self.tail = None
        self.size_list = 0
        self.UpdateTail()

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
            var_sort += "sorted"
        else:
            var_sort += "not sorted"
        print(
            "The length of the list: ",
            self.size_list,
            "\nThe list is",
            var_sort,
        )
        curr = self.head
        print("The contents of the list are: ", end="")
        while curr is not None:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

    def UpdateTail(self):
        if self.head is None:
            return
        else:
            curr = self.head
            while curr.next is not None and curr.next != self.head:
                curr = curr.next
            self.tail = curr
