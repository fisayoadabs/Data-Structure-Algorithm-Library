from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

class Heap:
    elements =[]
    def __init__(self, size=0, array=None):
        if array is None:
            self.elements = []
        else:
            self.elements = self.heapify(array)

    def parent(self, i):
        return ((i-1)//2)

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def swap(self, x, y):
        self.elements[x], self.elements[y] = self.elements[y], self.elements[x]

    def heapify_down(self, i):
        while self.left(i) < len(self.elements):
            left = self.left(i)
            right = self.right(i)
            if right < len(self.elements) and self.compare(self.elements[right], self.elements[left]):
                child = right
            else:
                child = left
            if self.compare(self.elements[child], self.elements[i]):
                self.swap(i, child)
                i = child
            else:
                break
    
    

    def heapify_up(self, i):
        while i > 0 and self.compare(self.elements[i], self.elements[self.parent(i)]):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify(self, array):
        pile = array.copy()
        n = len(pile)

        for i in range(n//2 - 1, -1, -1):
            self.heapify_down(i)

        return pile

    def getSize(self):
        print(len(self.elements))

    def isEmpty(self):
        if (len(self.elements) == 0):
            print("The list is empty")
        else:
            print("The list is not empty")
        return

    def clear(self):
        self.elements = []

    def contains(self, i):
        if(i in self.elements):
            print(i, "was found")
        else:
            print(i, "was not found")
        return 

    def insert(self, key):
        self.elements.append(key)
        self.heapify_up(len(self.elements)-1)

    def delete(self, key):
        index = self.elements.index(key) if key in self.elements else -1
        if index != -1:
            last = len(self.elements)-1
            self.swap(index, last)
            self.elements.pop()
            self.heapify_down(index)

    def sort(self):
        n = len(self.elements)
        for i in range(n-1, 0, -1):
            self.swap(0, i)
            self.heapify_down(0)

    def print(self):
        for i in range(len(self.elements)):
            print(self.parent(i), end=" ")
        print()
        for i in range(len(self.elements)):
            print(self.elements[i], end=" ")
        print()
