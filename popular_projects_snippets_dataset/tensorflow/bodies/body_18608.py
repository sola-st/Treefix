# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""See `SummaryWriter.set_as_default`."""
if context.executing_eagerly() and self._closed:
    raise RuntimeError(f"SummaryWriter {self!r} is already closed")
super().set_as_default(step)
