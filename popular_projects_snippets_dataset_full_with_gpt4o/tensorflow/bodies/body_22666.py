# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
self.AddOp(op)
if self._outer_context:
    self._outer_context.AddInnerOp(op)
