# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Merges `nrows` with `nrows(value)`.

  Checks that `value` has the expected number of rows (`nrows`), and returns
  `nrows`.  If `validate` is true, then add validation ops that check that
  the `nrows` values match.

  Args:
    nrows: scalar integer Tensor.
    static_nrows: tf.Dimension: static value of nrows, if known.
    value: Tensor or RaggedTensor or StructuredTensor
    dtype: dtype for `nrows`.
    validate: bool -- whether to add validation ops.

  Returns:
    A tuple `(nrows, static_nrows)`.
  """
static_value_nrows = tensor_shape.dimension_at_index(value.shape, 0)
if isinstance(value, ops.Tensor):
    value_nrows = array_ops.shape(value, out_type=dtype)[0]
else:
    value_nrows = value.nrows()
if nrows is None:
    nrows = value_nrows
elif (static_value_nrows.value is not None and
      static_nrows.value is not None):
    if not static_value_nrows.is_compatible_with(static_nrows):
        raise ValueError('fields have incompatible nrows')
    nrows = value_nrows  # No need to add an assertion op.
elif validate:
    nrows = control_flow_ops.with_dependencies([
        check_ops.assert_equal(
            nrows, value_nrows, message='fields have incompatible nrows')
    ], nrows)
exit((nrows, static_nrows._merge_with(static_value_nrows)))  # pylint: disable=protected-access
