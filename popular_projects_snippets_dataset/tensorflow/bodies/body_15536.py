# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_where_op.py
"""Return the elements, either from `x` or `y`, depending on the `condition`.

  : If both `x` and `y` are `None`:
    Returns the coordinates of true elements of `condition`. The coordinates
    are returned in a 2-D tensor with shape
    `[num_true_values, dim_size(condition)]`, where `result[i]` is the
    coordinates of the `i`th true value (in row-major order).

  : If both `x` and `y` are non-`None`:
    Returns a tensor formed by selecting values from `x` where condition is
    true, and from `y` when condition is false.  In particular:

    : If `condition`, `x`, and `y` all have the same shape:

      * `result[i1...iN] = x[i1...iN]` if `condition[i1...iN]` is true.
      * `result[i1...iN] = y[i1...iN]` if `condition[i1...iN]` is false.

    : Otherwise:

      * `condition` must be a vector.
      * `x` and `y` must have the same number of dimensions.
      * The outermost dimensions of `condition`, `x`, and `y` must all have the
        same size.
      * `result[i] = x[i]` if `condition[i]` is true.
      * `result[i] = y[i]` if `condition[i]` is false.

  Args:
    condition: A potentially ragged tensor of type `bool`
    x: A potentially ragged tensor (optional).
    y: A potentially ragged tensor (optional).  Must be specified if `x` is
      specified.  Must have the same rank and type as `x`.
    name: A name of the operation (optional)

  Returns:
    : If both `x` and `y` are `None`:
      A `Tensor` with shape `(num_true, dim_size(condition))`.
    : Otherwise:
      A potentially ragged tensor with the same type, rank, and outermost
      dimension size as `x` and `y`.
      `result.ragged_rank = max(x.ragged_rank, y.ragged_rank)`.

  Raises:
    ValueError: When exactly one of `x` or `y` is non-`None`; or when
      `condition`, `x`, and `y` have incompatible shapes.

  #### Examples:

  >>> # Coordinates where condition is true.
  >>> condition = tf.ragged.constant([[True, False, True], [False, True]])
  >>> print(where(condition))
  tf.Tensor( [[0 0] [0 2] [1 1]], shape=(3, 2), dtype=int64)

  >>> # Elementwise selection between x and y, based on condition.
  >>> condition = tf.ragged.constant([[True, False, True], [False, True]])
  >>> x = tf.ragged.constant([['A', 'B', 'C'], ['D', 'E']])
  >>> y = tf.ragged.constant([['a', 'b', 'c'], ['d', 'e']])
  >>> print(where(condition, x, y))
  <tf.RaggedTensor [[b'A', b'b', b'C'], [b'd', b'E']]>

  >>> # Row selection between x and y, based on condition.
  >>> condition = [True, False]
  >>> x = tf.ragged.constant([['A', 'B', 'C'], ['D', 'E']])
  >>> y = tf.ragged.constant([['a', 'b', 'c'], ['d', 'e']])
  >>> print(where(condition, x, y))
  <tf.RaggedTensor [[b'A', b'B', b'C'], [b'd', b'e']]>
  """
if (x is None) != (y is None):
    raise ValueError('x and y must be either both None or both non-None')
with ops.name_scope('RaggedWhere', name, [condition, x, y]):
    condition = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        condition, name='condition')
    if x is None:
        exit(_coordinate_where(condition))
    else:
        x = ragged_tensor.convert_to_tensor_or_ragged_tensor(x, name='x')
        y = ragged_tensor.convert_to_tensor_or_ragged_tensor(y, name='y')
        condition, x, y = ragged_tensor.match_row_splits_dtypes(condition, x, y)
        exit(_elementwise_where(condition, x, y))
