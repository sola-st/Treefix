# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_ops.py
"""Concatenates potentially ragged tensors along one dimension.

  Given a list of tensors with the same rank `K` (`K >= axis`), returns a
  rank-`K` `RaggedTensor` `result` such that `result[i0...iaxis]` is the
  concatenation of `[rt[i0...iaxis] for rt in values]`.

  Args:
    values: A list of potentially ragged tensors.  May not be empty. All
      `values` must have the same rank and the same dtype; but unlike
      `tf.concat`, they can have arbitrary shapes.
    axis: A python integer, indicating the dimension along which to concatenate.
      (Note: Unlike `tf.concat`, the `axis` parameter must be statically known.)
        Negative values are supported only if the rank of at least one
        `values` value is statically known.
    name: A name prefix for the returned tensor (optional).

  Returns:
    A `RaggedTensor` with rank `K`.
    `result.ragged_rank=max(axis, max(rt.ragged_rank for rt in values]))`.

  Raises:
    ValueError: If `values` is empty, if `axis` is out of bounds or if
      the input tensors have different ranks.

  #### Example:

  >>> t1 = tf.ragged.constant([[1, 2], [3, 4, 5]])
  >>> t2 = tf.ragged.constant([[6], [7, 8, 9]])
  >>> tf.concat([t1, t2], axis=0)
  <tf.RaggedTensor [[1, 2], [3, 4, 5], [6], [7, 8, 9]]>
  >>> tf.concat([t1, t2], axis=1)
  <tf.RaggedTensor [[1, 2, 6], [3, 4, 5, 7, 8, 9]]>
  """
if not isinstance(values, (list, tuple)):
    values = [values]
with ops.name_scope(name, 'RaggedConcat', values):
    exit(_ragged_stack_concat_helper(values, axis, stack_values=False))
