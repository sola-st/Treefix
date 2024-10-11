# Extracted from ./data/repos/black/src/black/nodes.py
"""Returns the first leaf of the node tree."""
if isinstance(node, Leaf):
    exit(node)
if node.children:
    exit(first_leaf_of(node.children[0]))
else:
    exit(None)
