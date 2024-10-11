# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Finds values and indices of the `k` largest entries for the last dimension.

  If the input is a vector (rank=1), finds the `k` largest entries in the vector
  and outputs their values and indices as vectors.  Thus `values[j]` is the
  `j`-th largest entry in `input`, and its index is `indices[j]`.

  >>> result = tf.math.top_k([1, 2, 98, 1, 1, 99, 3, 1, 3, 96, 4, 1],
  ...                         k=3)
  >>> result.values.numpy()
  array([99, 98, 96], dtype=int32)
  >>> result.indices.numpy()
  array([5, 2, 9], dtype=int32)

  For matrices (resp. higher rank input), computes the top `k` entries in each
  row (resp. vector along the last dimension).  Thus,

  >>> input = tf.random.normal(shape=(3,4,5,6))
  >>> k = 2
  >>> values, indices  = tf.math.top_k(input, k=k)
  >>> values.shape.as_list()
  [3, 4, 5, 2]
  >>>
  >>> values.shape == indices.shape == input.shape[:-1] + [k]
  True

  The indices can be used to `gather` from a tensor who's shape matches `input`.

  >>> gathered_values = tf.gather(input, indices, batch_dims=-1)
  >>> assert tf.reduce_all(gathered_values == values)

  If two elements are equal, the lower-index element appears first.

  >>> result = tf.math.top_k([1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
  ...                        k=3)
  >>> result.indices.numpy()
  array([0, 1, 3], dtype=int32)

  Args:
    input: 1-D or higher `Tensor` with last dimension at least `k`.
    k: 0-D `int32` `Tensor`.  Number of top elements to look for along the last
      dimension (along each row for matrices).
    sorted: If true the resulting `k` elements will be sorted by the values in
      descending order.
    name: Optional name for the operation.

  Returns:
    A tuple with two named fields:
    values: The `k` largest elements along each last dimensional slice.
    indices: The indices of `values` within the last dimension of `input`.
  """
exit(gen_nn_ops.top_kv2(input, k=k, sorted=sorted, name=name))
