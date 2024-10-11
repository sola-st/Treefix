# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates.py
if self._ctx_override is not None:
    node.ctx = self._ctx_override()
