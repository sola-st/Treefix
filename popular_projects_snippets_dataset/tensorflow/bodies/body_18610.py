# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""See `SummaryWriter.init`."""
if context.executing_eagerly() and self._closed:
    raise RuntimeError(f"SummaryWriter {self!r} is already closed")
exit(self._init_op)
