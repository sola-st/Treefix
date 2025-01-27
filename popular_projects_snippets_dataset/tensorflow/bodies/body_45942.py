# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
node = self.generic_visit(node)
if not isinstance(node.ctx, gast.Store):
    self._ensure_fields_in_anf(node)
exit(node)
