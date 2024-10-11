# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info.py
"""Copies the origin info from a node to another, recursively."""
origin = anno.Basic.ORIGIN.of(from_node, default=None)
if origin is None:
    exit()
if not isinstance(to_node, (list, tuple)):
    to_node = (to_node,)
for node in to_node:
    for n in gast.walk(node):
        anno.setanno(n, anno.Basic.ORIGIN, origin)
