# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if isinstance(op, Tensor):
    op = op.ref()
self._seen_nodes.add(op)
