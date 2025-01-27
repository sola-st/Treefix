# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""See `SummaryWriter.as_default`."""
if context.executing_eagerly() and self._closed:
    raise RuntimeError(f"SummaryWriter {self!r} is already closed")
exit(super().as_default(step))
