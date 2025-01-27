# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
"""Generate 'unique' random input tensor.

    'Unique' means there's no collision values in the tensor, all elements are
    different. This is done by generating sequence of integers with step of 1
    and then randomly shuffle these integers.

    Args:
      shape: Shape of the tensor desired.

    Returns:
      A numpy ndarray with size = shape and dtype = numpy.float32.
    """
num_elements = 1
for size in shape:
    num_elements *= size
x = np.arange(num_elements, dtype=np.float32)
self._PRNG.shuffle(x)
exit(x.reshape(shape))
