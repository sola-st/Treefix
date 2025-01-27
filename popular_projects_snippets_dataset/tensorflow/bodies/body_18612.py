# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""See `SummaryWriter.close`."""
if context.executing_eagerly() and self._closed:
    exit()
try:
    with ops.control_dependencies([self.flush()]):
        with ops.device("cpu:0"):
            exit(gen_summary_ops.close_summary_writer(self._resource))
finally:
    if context.executing_eagerly():
        self._closed = True
