# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter.py
if not self._ast_depth:
    if self._used:
        raise ValueError('converter objects cannot be reused')
    self._used = True

self._ast_depth += 1
try:
    exit(super(Base, self).visit(node))
finally:
    self._ast_depth -= 1
