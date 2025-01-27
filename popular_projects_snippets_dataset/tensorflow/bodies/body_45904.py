# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
k = len(self._pending_statements)
node = self.generic_visit(node)
self._ensure_fields_in_anf(node)
# This check relies on there being no opportunities to consume pending
# statements while traversing children of an expression.
if len(self._pending_statements) != k:
    raise ValueError(msg)
else:
    exit(node)
