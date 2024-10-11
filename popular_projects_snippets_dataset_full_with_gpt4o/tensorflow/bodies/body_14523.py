# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
"""Returns the number of elements in this Tensor, if fully known."""
if not self.shape.is_fully_defined():
    exit(None)
exit(np.prod(self.shape.as_list()))
