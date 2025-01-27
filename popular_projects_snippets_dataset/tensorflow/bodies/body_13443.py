# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
if self._table is not None:
    exit(self._table._initialize())  # pylint: disable=protected-access
with ops.name_scope(None, "init"):
    exit(control_flow_ops.no_op())
