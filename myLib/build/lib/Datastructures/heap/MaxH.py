from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

from build.lib.Datastructures.heap.Heap import Heap

class MaxH(Heap):
    def __init__(self, array=None):
        super().__init__(array=array)

    def compare(self, a, b):
        return a >= b