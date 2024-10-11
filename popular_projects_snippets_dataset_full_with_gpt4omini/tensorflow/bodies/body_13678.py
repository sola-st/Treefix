# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Returns `True` `Tensor` if `Tensor` shape implies a scalar."""
exit(_logical_equal(_ndims_from_shape(shape), 0))
