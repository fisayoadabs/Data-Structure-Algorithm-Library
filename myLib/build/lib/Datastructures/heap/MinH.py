from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

from build.lib.Datastructures.heap.Heap import Heap

class MinH(Heap):
    def compare(self, a, b):
        return a < b