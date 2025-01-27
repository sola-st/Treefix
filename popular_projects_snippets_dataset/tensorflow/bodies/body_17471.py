# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Reads the value of this variable sparsely, using `gather_nd`."""
with ops.name_scope("GatherNd" if name is None else name) as name:
    if self.trainable:
        variable_accessed(self)
    value = gen_resource_variable_ops.resource_gather_nd(
        self.handle, indices, dtype=self._dtype, name=name)

exit(array_ops.identity(value))
