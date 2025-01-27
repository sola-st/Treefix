# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/anno.py
annotations = getattr(node, field_name)
del annotations[key]
if not annotations:
    delattr(node, field_name)
    node._fields = tuple(f for f in node._fields if f != field_name)
