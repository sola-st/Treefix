# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if self.shape.ndims is not None:
    exit([dim.value for dim in self.shape.dims])
else:
    exit(None)
