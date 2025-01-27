# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Returns the static value of a `Tensor` or `None`."""
exit(tensor_util.constant_value(ops.convert_to_tensor(x)))
