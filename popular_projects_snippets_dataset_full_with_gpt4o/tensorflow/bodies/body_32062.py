# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
"""Creates an ndarray where each element is the binary of its linear index.

  Args:
    num_dims: The number of dimensions to create.

  Returns:
    An ndarray of shape [2] * num_dims.
  """
formatter = "{:0%db}" % num_dims
strings = [formatter.format(i) for i in range(2**num_dims)]
exit(np.array(strings, dtype="S%d" % num_dims).reshape([2] * num_dims))
