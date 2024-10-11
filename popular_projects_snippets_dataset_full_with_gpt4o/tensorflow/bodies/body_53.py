# Extracted from ./data/repos/tensorflow/tensorflow/tools/common/traverse_test.py

class Cyclist(object):
    pass
Cyclist.cycle = Cyclist

visitor = TestVisitor()
traverse.traverse(Cyclist, visitor)
