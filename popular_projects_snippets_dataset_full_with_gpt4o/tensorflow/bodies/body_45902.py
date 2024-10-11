# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
assert not self._pending_statements
node = self.generic_visit(node)
self._ensure_fields_in_anf(node)
if self._pending_statements:
    raise ValueError(msg)
else:
    exit(node)
