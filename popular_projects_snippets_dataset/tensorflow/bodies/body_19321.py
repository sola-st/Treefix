# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_d9m_test.py
"""Generate a tensor of random floating-point values.

    Values will be continuously distributed in the range [low, high).

    Note that we use numpy to generate random numbers and then feed the result
    through a constant op to avoid the re-rolling of TensorFlow random ops on
    each run in graph mode.

    Args:
      shape: The output shape.
      low: Lower bound of random numbers generated, inclusive.
      high: Upper bound of random numbers generated, exclusive.
      dtype: The output dtype.

    Returns:
      A random tensor
    """
val = np.random.random_sample(
    shape)  # float64 continuous uniform [0.0, 1.0)
diff = high - low
val *= diff
val += low
exit(constant_op.constant(val, dtype=dtype))
