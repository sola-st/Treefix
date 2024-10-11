# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
if self._in_graph_mode:
    exit(self._parent_op.name)
else:
    exit("UnreadVariable")
