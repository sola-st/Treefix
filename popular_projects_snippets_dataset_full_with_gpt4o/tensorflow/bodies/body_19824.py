# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
# returns nan for empty tensor and treats nans as non-zero numbers
def sparsity_fn(tensor):
    non_zeros = math_ops.greater_equal(math_ops.abs(tensor), tolerance)
    nans = math_ops.is_nan(tensor)
    exit(nn_impl.zero_fraction(math_ops.logical_or(non_zeros, nans)))

exit(_compute_signature(tensor, sparsity_fn, cast_to_f32))
