class TNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def __init__(self, val):
        self.root = TNode(val)
        
    def __init__(self, obj):
        self.root = obj
        
    def set_root(self, obj):
        self.root = obj
        
    def get_root(self):
        return self.root
    
    def insert(self, val):
        if self.root is None:
            self.root = TNode(val)
            return
        curr = self.root
        while curr is not None:
            if val < curr.val:
                if curr.left is None:
                    curr.left = TNode(val)
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TNode(val)
                    return
                curr = curr.right
                
    def insert_node(self, node):
        if self.root is None:
            self.root = node
            return
        curr = self.root
        while curr is not None:
            if node.val < curr.val:
                if curr.left is None:
                    curr.left = node
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = node
                    return
                curr = curr.right
                
    def delete(self, val):
        if self.root is None:
            print("Value not found in the tree")
            return
        parent = None
        curr = self.root
        while curr is not None and curr.val != val:
            parent = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if curr is None:
            print("Value not found in the tree")
            return
        if curr.left is None and curr.right is None:
            if curr == self.root:
                self.root = None
            elif curr == parent.left:
                parent.left = None
            else:
                parent.right = None
        elif curr.left is None:
            if curr == self.root:
                self.root = curr.right
            elif curr == parent.left:
                parent.left = curr.right
            else:
                parent.right = curr.right
        elif curr.right is None:
            if curr == self.root:
                self.root = curr.left
            elif curr == parent.left:
                parent.left = curr.left
            else:
                parent.right = curr.left
        else:
            successor_parent = curr
            successor = curr.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            if successor == curr.right:
                successor.left = curr.left
            else:
                successor_parent.left = successor.right
                successor.left = curr.left
                successor.right = curr.right
            if curr == self.root:
                self.root = successor
            elif curr == parent.left:
                parent.left = successor
            else:
                parent.right = successor
                
    def search(self, val):
        curr = self.root
        while curr is not None and curr.val != val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr
    
    def print_in_order(self):
        def traverse(node):
            if node is not None:
                traverse(node.left)
                print(node.val, end=' ')
                traverse(node.right)
        traverse(self.root)
        print()
        
    def print_bf(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            curr = queue.pop(0)
            print(curr.val, end=' ')
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
            if len(queue) == 0:
                print()




