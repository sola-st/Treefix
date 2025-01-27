# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
assert not self._pending_statements
node = self.generic_visit(node)
if children_ok_to_transform:
    self._ensure_fields_in_anf(node)
results = self._consume_pending_statements()
results.append(node)
exit(results)
