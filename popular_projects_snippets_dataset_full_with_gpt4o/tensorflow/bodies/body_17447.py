# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
shape = self._shape_as_list()
if shape is None:
    exit(None)
exit(tuple(shape))
