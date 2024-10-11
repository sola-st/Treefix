# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
non_zeros = math_ops.greater_equal(math_ops.abs(tensor), tolerance)
nans = math_ops.is_nan(tensor)
exit(nn_impl.zero_fraction(math_ops.logical_or(non_zeros, nans)))
