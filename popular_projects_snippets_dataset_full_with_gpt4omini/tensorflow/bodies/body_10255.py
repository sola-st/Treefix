# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops.py
"""Returns the indices of a tensor that give its sorted order along an axis.

  >>> values = [1, 10, 26.9, 2.8, 166.32, 62.3]
  >>> sort_order = tf.argsort(values)
  >>> sort_order.numpy()
  array([0, 3, 1, 2, 5, 4], dtype=int32)

  For a 1D tensor:

  >>> sorted = tf.gather(values, sort_order)
  >>> assert tf.reduce_all(sorted == tf.sort(values))

  For higher dimensions, the output has the same shape as
  `values`, but along the given axis, values represent the index of the sorted
  element in that slice of the tensor at the given position.

  >>> mat = [[30,20,10],
  ...        [20,10,30],
  ...        [10,30,20]]
  >>> indices = tf.argsort(mat)
  >>> indices.numpy()
  array([[2, 1, 0],
         [1, 0, 2],
         [0, 2, 1]], dtype=int32)

  If `axis=-1` these indices can be used to apply a sort using `tf.gather`:

  >>> tf.gather(mat, indices, batch_dims=-1).numpy()
  array([[10, 20, 30],
         [10, 20, 30],
         [10, 20, 30]], dtype=int32)

  See also:

    * `tf.sort`: Sort along an axis.
    * `tf.math.top_k`: A partial sort that returns a fixed number of top values
      and corresponding indices.

  Args:
    values: 1-D or higher **numeric** `Tensor`.
    axis: The axis along which to sort. The default is -1, which sorts the last
      axis.
    direction: The direction in which to sort the values (`'ASCENDING'` or
      `'DESCENDING'`).
    stable: If True, equal elements in the original tensor will not be
      re-ordered in the returned order. Unstable sort is not yet implemented,
      but will eventually be the default for performance reasons. If you require
      a stable order, pass `stable=True` for forwards compatibility.
    name: Optional name for the operation.

  Returns:
    An int32 `Tensor` with the same shape as `values`. The indices that would
        sort each slice of the given `values` along the given `axis`.

  Raises:
    ValueError: If axis is not a constant scalar, or the direction is invalid.
    tf.errors.InvalidArgumentError: If the `values.dtype` is not a `float` or
        `int` type.
  """
del stable  # Unused.
with framework_ops.name_scope(name, 'argsort'):
    exit(_sort_or_argsort(values, axis, direction, return_argsort=True))
