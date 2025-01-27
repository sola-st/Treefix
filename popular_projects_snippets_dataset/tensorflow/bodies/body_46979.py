# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/anno.py
if not hasattr(node, field_name):
    exit(frozenset())
exit(frozenset(getattr(node, field_name).keys()))
