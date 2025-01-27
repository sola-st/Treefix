# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_ops.py
"""Stacks a list of rank-`R` tensors into one rank-`(R+1)` `RaggedTensor`.

  Given a list of tensors or ragged tensors with the same rank `R`
  (`R >= axis`), returns a rank-`R+1` `RaggedTensor` `result` such that
  `result[i0...iaxis]` is `[value[i0...iaxis] for value in values]`.

  #### Examples:

  >>> # Stacking two ragged tensors.
  >>> t1 = tf.ragged.constant([[1, 2], [3, 4, 5]])
  >>> t2 = tf.ragged.constant([[6], [7, 8, 9]])
  >>> tf.ragged.stack([t1, t2], axis=0)
  <tf.RaggedTensor [[[1, 2], [3, 4, 5]], [[6], [7, 8, 9]]]>
  >>> tf.ragged.stack([t1, t2], axis=1)
  <tf.RaggedTensor [[[1, 2], [6]], [[3, 4, 5], [7, 8, 9]]]>

  >>> # Stacking two dense tensors with different sizes.
  >>> t3 = tf.constant([[1, 2, 3], [4, 5, 6]])
  >>> t4 = tf.constant([[5], [6], [7]])
  >>> tf.ragged.stack([t3, t4], axis=0)
  <tf.RaggedTensor [[[1, 2, 3], [4, 5, 6]], [[5], [6], [7]]]>

  Args:
    values: A list of `tf.Tensor` or `tf.RaggedTensor`.  May not be empty. All
      `values` must have the same rank and the same dtype; but unlike
      `tf.stack`, they can have arbitrary dimension sizes.
    axis: A python integer, indicating the dimension along which to stack.
      (Note: Unlike `tf.stack`, the `axis` parameter must be statically known.)
      Negative values are supported only if the rank of at least one
      `values` value is statically known.
    name: A name prefix for the returned tensor (optional).

  Returns:
    A `RaggedTensor` with rank `R+1` (if `R>0`).
    If `R==0`, then the result will be returned as a 1D `Tensor`, since
    `RaggedTensor` can only be used when `rank>1`.
    `result.ragged_rank=1+max(axis, max(rt.ragged_rank for rt in values]))`.

  Raises:
    ValueError: If `values` is empty, if `axis` is out of bounds or if
      the input tensors have different ranks.
  """
if not isinstance(values, (list, tuple)):
    values = [values]
with ops.name_scope(name, 'RaggedConcat', values):
    exit(_ragged_stack_concat_helper(values, axis, stack_values=True))
