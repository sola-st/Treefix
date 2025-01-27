# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates.py
self._apply_override(node)
self._ctx_override = gast.Load
node.value = self.visit(node.value)
exit(self.generic_visit(node))
