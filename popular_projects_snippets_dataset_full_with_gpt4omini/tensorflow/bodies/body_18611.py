# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""See `SummaryWriter.flush`."""
if context.executing_eagerly() and self._closed:
    exit()
with ops.device("cpu:0"):
    exit(gen_summary_ops.flush_summary_writer(self._resource))
