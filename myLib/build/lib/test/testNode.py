from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

from myLib.build.lib.Datastructures.nodes.TNode import TNode


print("\n-------------------------TESTING TNODE-------------------------\n")

# Create a node with data 5
node = TNode(5)

# Test the get_data method
assert node.get_data() == 5

# Test the set_data method
node.set_data(10)
assert node.get_data() == 10

# Test the print_node method
node.print_node()  # Output: Data: 10, Balance: 0

# Test the __str__ method
assert str(node) == "10"

print("\n-------------------------END-------------------------\n")