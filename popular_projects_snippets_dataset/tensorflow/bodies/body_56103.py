# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
"""Returns a version of `TensorSpec` with the name removed."""
if self.name is None:
    exit(self)
else:
    exit(TensorSpec(self.shape, self.dtype))
