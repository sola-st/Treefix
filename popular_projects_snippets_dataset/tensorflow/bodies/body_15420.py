# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Inserts a dimension with shape 1 into a potentially ragged tensor's shape.

  Given a potentially ragged tenor `input`, this operation inserts a
  dimension with size 1 at the dimension `axis` of `input`'s shape.

  The following table gives some examples showing how `ragged.expand_dims`
  impacts the shapes of different input tensors.  Ragged dimensions are
  indicated by enclosing them in parentheses.

  input.shape             | axis | result.shape
  ----------------------- | ---- | -----------------------------
  `[D1, D2]`              |  `0` | `[1, D1, D2]`
  `[D1, D2]`              |  `1` | `[D1, 1, D2]`
  `[D1, D2]`              |  `2` | `[D1, D2, 1]`
  `[D1, (D2), (D3), D4]`  |  `0` | `[1, D1, (D2), (D3), D4]`
  `[D1, (D2), (D3), D4]`  |  `1` | `[D1, 1, (D2), (D3), D4]`
  `[D1, (D2), (D3), D4]`  |  `2` | `[D1, (D2), 1, (D3), D4]`
  `[D1, (D2), (D3), D4]`  |  `3` | `[D1, (D2), (D3), 1, D4]`
  `[D1, (D2), (D3), D4]`  |  `4` | `[D1, (D2), (D3), D4, 1]`

  Args:
    input: The potentially tensor that should be expanded with a new dimension.
    axis: An integer constant indicating where the new dimension should be
      inserted.
    name: A name for the operation (optional).

  Returns:
    A tensor with the same values as `input`, with an added dimension of
    size 1 at `axis`.

  #### Examples:

  >>> rt = tf.ragged.constant([[1, 2], [3]])
  >>> print(rt.shape)
  (2, None)

  >>> expanded = tf.expand_dims(rt, axis=0)
  >>> print(expanded.shape, expanded)
  (1, 2, None) <tf.RaggedTensor [[[1, 2], [3]]]>

  >>> expanded = tf.expand_dims(rt, axis=1)
  >>> print(expanded.shape, expanded)
  (2, 1, None) <tf.RaggedTensor [[[1, 2]], [[3]]]>

  >>> expanded = tf.expand_dims(rt, axis=2)
  >>> print(expanded.shape, expanded)
  (2, None, 1) <tf.RaggedTensor [[[1], [2]], [[3]]]>
  """
with ops.name_scope(name, 'RaggedExpandDims', [input]):
    input = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        input, name='input')

    if not ragged_tensor.is_ragged(input):
        exit(array_ops.expand_dims(input, axis))

    ndims = None if input.shape.ndims is None else input.shape.ndims + 1
    axis = array_ops.get_positive_axis(axis, ndims, ndims_name='rank(input)')

    if axis == 0:
        exit(ragged_tensor.RaggedTensor.from_uniform_row_length(
            input, uniform_row_length=input.nrows(), nrows=1, validate=False))
    elif axis == 1:
        exit(ragged_tensor.RaggedTensor.from_uniform_row_length(
            input, uniform_row_length=1, nrows=input.nrows(), validate=False))
    else:
        if ragged_tensor.is_ragged(input.values):
            exit(input.with_values(expand_dims(input.values, axis - 1)))
        else:
            exit(input.with_values(array_ops.expand_dims(input.values, axis - 1)))
