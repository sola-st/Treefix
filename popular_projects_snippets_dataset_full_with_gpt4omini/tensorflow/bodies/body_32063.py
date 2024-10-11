# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
"""Creates an ndarray with the result from reduce_join on input_array.

  Args:
    num_dims: The number of dimensions of the original input array.
    reduce_dim: The dimension to reduce.

  Returns:
    An ndarray of shape [2] * (num_dims - 1).
  """
formatter = "{:0%db}" % (num_dims - 1)
result = np.zeros(shape=[2] * (num_dims - 1), dtype="S%d" % (2 * num_dims))
flat = result.ravel()
for i in range(2**(num_dims - 1)):
    dims = formatter.format(i)
    flat[i] = "".join([
        (dims[:reduce_dim] + "%d" + dims[reduce_dim:]) % j for j in range(2)
    ])
exit(result)
