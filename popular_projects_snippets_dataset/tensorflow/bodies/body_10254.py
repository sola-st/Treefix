# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops.py
"""Sorts a tensor.

  Usage:

  >>> a = [1, 10, 26.9, 2.8, 166.32, 62.3]
  >>> tf.sort(a).numpy()
  array([  1.  ,   2.8 ,  10.  ,  26.9 ,  62.3 , 166.32], dtype=float32)

  >>> tf.sort(a, direction='DESCENDING').numpy()
  array([166.32,  62.3 ,  26.9 ,  10.  ,   2.8 ,   1.  ], dtype=float32)

  For multidimensional inputs you can control which axis the sort is applied
  along. The default `axis=-1` sorts the innermost axis.

  >>> mat = [[3,2,1],
  ...        [2,1,3],
  ...        [1,3,2]]
  >>> tf.sort(mat, axis=-1).numpy()
  array([[1, 2, 3],
         [1, 2, 3],
         [1, 2, 3]], dtype=int32)
  >>> tf.sort(mat, axis=0).numpy()
  array([[1, 1, 1],
         [2, 2, 2],
         [3, 3, 3]], dtype=int32)

  See also:

    * `tf.argsort`: Like sort, but it returns the sort indices.
    * `tf.math.top_k`: A partial sort that returns a fixed number of top values
      and corresponding indices.


  Args:
    values: 1-D or higher **numeric** `Tensor`.
    axis: The axis along which to sort. The default is -1, which sorts the last
      axis.
    direction: The direction in which to sort the values (`'ASCENDING'` or
      `'DESCENDING'`).
    name: Optional name for the operation.

  Returns:
    A `Tensor` with the same dtype and shape as `values`, with the elements
        sorted along the given `axis`.

  Raises:
    tf.errors.InvalidArgumentError: If the `values.dtype` is not a `float` or
        `int` type.
    ValueError: If axis is not a constant scalar, or the direction is invalid.
  """
with framework_ops.name_scope(name, 'sort'):
    exit(_sort_or_argsort(values, axis, direction, return_argsort=False))
