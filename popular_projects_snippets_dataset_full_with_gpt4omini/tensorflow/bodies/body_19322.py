# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_d9m_test.py
"""Generate a tensor of random 32-bit integer values.

    Note that we use numpy to generate random numbers and then feed the result
    through a constant op to avoid the re-rolling of TensorFlow random ops on
    each run in graph mode.

    Args:
      shape: The output shape.
      low: Lower bound of random numbers generated, inclusive.
      high: Upper bound of random numbers generated, exclusive.

    Returns:
      A random tensor
    """
val = np.random.randint(low=low, high=high, size=shape)
exit(constant_op.constant(val, dtype=dtypes.int32))
