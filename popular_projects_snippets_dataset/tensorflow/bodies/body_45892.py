# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
"""Computes whether this pattern matches the given edge."""
if self.parent is ANY or isinstance(parent, self.parent):
    pass  # OK
else:
    exit(False)
if self.field is ANY or field == self.field:
    pass  # OK
else:
    exit(False)
exit(self.child is ANY or isinstance(child, self.child))
