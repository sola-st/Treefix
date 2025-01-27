# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser.py
if node is None:
    exit(None)
if isinstance(node, gast.Name):
    exit(node.id)
assert isinstance(node, str)
exit(node)
