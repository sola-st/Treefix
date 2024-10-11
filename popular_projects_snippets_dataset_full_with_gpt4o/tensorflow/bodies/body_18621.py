# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""See `SummaryWriter.close`."""
with ops.control_dependencies([self.flush()]):
    with ops.device("cpu:0"):
        exit(gen_summary_ops.close_summary_writer(self._resource))
