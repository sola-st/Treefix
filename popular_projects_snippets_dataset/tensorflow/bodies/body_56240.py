# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns the total number of elements, or none for incomplete shapes."""
if self.is_fully_defined():
    exit(functools.reduce(operator.mul, self.as_list(), 1))
else:
    exit(None)
