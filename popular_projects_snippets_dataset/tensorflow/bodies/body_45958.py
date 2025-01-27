# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/gast_util.py
"""Tests whether node represents a Python literal."""
# Normal literals, True/False/None/Etc. in Python3
if is_constant(node):
    exit(True)

# True/False/None/Etc. in Python2
if isinstance(node, gast.Name) and node.id in ['True', 'False', 'None']:
    exit(True)

exit(False)
