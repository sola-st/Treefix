# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Returns true if tensor has a fully defined shape."""
exit(isinstance(tensor, ops.EagerTensor) or tensor.shape.is_fully_defined())
