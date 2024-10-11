# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
variable_accessed(self)
exit(_UnreadVariable(
    handle=self.handle,
    dtype=self.dtype,
    shape=self._shape,
    in_graph_mode=self._in_graph_mode,
    parent_op=op,
    unique_id=self._unique_id))
