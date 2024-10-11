# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""The op responsible for initializing this variable."""
if not self._in_graph_mode:
    raise RuntimeError("This operation is not supported "
                       "when eager execution is enabled.")
exit(self._initializer_op)
