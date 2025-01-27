# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Creates a vector from a (batch of) triangular matrix.

  The vector is created from the lower-triangular or upper-triangular portion
  depending on the value of the parameter `upper`.

  If `x.shape` is `[b1, b2, ..., bB, n, n]` then the output shape is
  `[b1, b2, ..., bB, d]` where `d = n (n + 1) / 2`.

  Example:

  ```python
  fill_triangular_inverse(
    [[4, 0, 0],
     [6, 5, 0],
     [3, 2, 1]])

  # ==> [1, 2, 3, 4, 5, 6]

  fill_triangular_inverse(
    [[1, 2, 3],
     [0, 5, 6],
     [0, 0, 4]], upper=True)

  # ==> [1, 2, 3, 4, 5, 6]
  ```

  Args:
    x: `Tensor` representing lower (or upper) triangular elements.
    upper: Python `bool` representing whether output matrix should be upper
      triangular (`True`) or lower triangular (`False`, default).
    name: Python `str`. The name to give this op.

  Returns:
    flat_tril: (Batch of) vector-shaped `Tensor` representing vectorized lower
      (or upper) triangular elements from `x`.
  """

with ops.name_scope(name, "fill_triangular_inverse", values=[x]):
    x = ops.convert_to_tensor(x, name="x")
    if tensor_shape.dimension_value(
        x.shape.with_rank_at_least(2)[-1]) is not None:
        n = np.int32(x.shape.dims[-1].value)
        m = np.int32((n * (n + 1)) // 2)
        static_final_shape = x.shape[:-2].concatenate([m])
    else:
        n = array_ops.shape(x)[-1]
        m = (n * (n + 1)) // 2
        static_final_shape = x.shape.with_rank_at_least(2)[:-2].concatenate(
            [None])
    ndims = prefer_static_rank(x)
    if upper:
        initial_elements = x[..., 0, :]
        triangular_portion = x[..., 1:, :]
    else:
        initial_elements = array_ops.reverse(x[..., -1, :], axis=[ndims - 2])
        triangular_portion = x[..., :-1, :]
    rotated_triangular_portion = array_ops.reverse(
        array_ops.reverse(triangular_portion, axis=[ndims - 1]),
        axis=[ndims - 2])
    consolidated_matrix = triangular_portion + rotated_triangular_portion
    end_sequence = array_ops.reshape(
        consolidated_matrix,
        array_ops.concat([array_ops.shape(x)[:-2], [n * (n - 1)]], axis=0))
    y = array_ops.concat([initial_elements, end_sequence[..., :m - n]], axis=-1)
    y.set_shape(static_final_shape)
    exit(y)
