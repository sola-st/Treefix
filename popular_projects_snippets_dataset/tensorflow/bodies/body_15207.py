# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Returns a TensorShape representation of the shape."""
lengths = self.static_lengths(ragged_lengths=False)
if not lengths:
    exit(tensor_shape.TensorShape(()))
if lengths[-1] == Ellipsis:
    exit(tensor_shape.TensorShape(None))
exit(tensor_shape.TensorShape(lengths))
