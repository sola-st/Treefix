# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
if self.shape.ndims is None:
    exit(None)
exit([dim.value for dim in self.shape.dims])
