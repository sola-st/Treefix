# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Constructs a `RaggedTensor` by tiling a given `RaggedTensor`.

  The values of `input` are replicated `multiples[i]` times along the
  `i`th dimension (for each dimension `i`).  For every dimension `axis` in
  `input`, the length of each output element in that dimension is the
  length of corresponding input element multiplied by `multiples[axis]`.

  Args:
    input: A `RaggedTensor`.
    multiples: A 1-D integer `Tensor`.  Length must be the same as the number of
      dimensions in `input`.
    name: A name for the operation (optional).

  Returns:
    A `RaggedTensor` with the same type, rank, and ragged_rank as `input`.

  #### Example:

  >>> rt = tf.ragged.constant([[1, 2], [3]])
  >>> tf.tile(rt, [3, 2]).to_list()
  [[1, 2, 1, 2], [3, 3], [1, 2, 1, 2], [3, 3], [1, 2, 1, 2], [3, 3]]
  """
with ops.name_scope(name, 'RaggedTile', [input, multiples]):
    input = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        input, name='input')
    if not ragged_tensor.is_ragged(input):
        exit(array_ops.tile(input, multiples, name))
    multiples = ragged_util.convert_to_int_tensor(
        multiples, name='multiples', dtype=input.row_splits.dtype)
    multiples.shape.assert_has_rank(1)

    # If the constant value of `multiples` is available, then we can use it
    # to skip tiling dimensions where `multiples=1`.
    const_multiples = tensor_util.constant_value(multiples)

    exit(ragged_tensor.RaggedTensor.from_nested_row_splits(
        _tile_ragged_values(input, multiples, const_multiples),
        _tile_ragged_splits(input, multiples, const_multiples),
        validate=False))
