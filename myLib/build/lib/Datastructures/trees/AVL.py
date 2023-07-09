from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

from build.lib.Datastructures.trees.BST import BST, TNode

class TNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL(BST):
    def __init__(self, val=None):
        if val is None:
            self.root = None
        elif isinstance(val, TNode):
            self.root = val
            self.balance_tree()
        else:
            self.root = TNode(val)
        
    def set_root(self, obj):
        self.root = obj
        if obj.left is not None or obj.right is not None:
            self.balance_tree()
        
    def get_root(self):
        return self.root
    
    def insert(self, val):
        super().insert(val)
        self.balance_tree()
        
    def insert_node(self, node):
        super().insert_node(node)
        self.balance_tree()
        
    def delete(self, val):
        super().delete(val)
        self.balance_tree()
        
    def balance_tree(self):
        def update_height(node):
            if node is None:
                return 0
            node.height = max(update_height(node.left), update_height(node.right)) + 1
            return node.height
        
        def get_balance(node):
            if node is None:
                return 0
            return update_height(node.left) - update_height(node.right)
        
        def rotate_left(node):
            new_root = node.right
            node.right = new_root.left
            new_root.left = node
            update_height(node)
            update_height(new_root)
            return new_root
        
        def rotate_right(node):
            new_root = node.left
            node.left = new_root.right
            new_root.right = node
            update_height(node)
            update_height(new_root)
            return new_root
        
        def balance(node):
            if node is None:
                return None
            if get_balance(node) > 1:
                if get_balance(node.left) < 0:
                    node.left = rotate_left(node.left)
                node = rotate_right(node)
            elif get_balance(node) < -1:
                if get_balance(node.right) > 0:
                    node.right = rotate_right(node.right)
                node = rotate_left(node)
            return node
        
        self.root = balance(self.root)
        
    def search(self, val):
        return super().search(val)
    
    def print_in_order(self):
        super().print_in_order()
        
    def print_bf(self):
        super().print_bf()


