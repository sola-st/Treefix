# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Generates feature cross from a list of tensors.

  The input tensors must have `rank=2`, and must all have the same number of
  rows.  The result is a `RaggedTensor` with the same number of rows as the
  inputs, where `result[row]` contains a list of all combinations of values
  formed by taking a single value from each input's corresponding row
  (`inputs[i][row]`).  Values are combined by joining their strings with '_X_'.
  E.g.:

  >>> tf.ragged.cross([tf.ragged.constant([['a'], ['b', 'c']]),
  ...                  tf.ragged.constant([['d'], ['e']]),
  ...                  tf.ragged.constant([['f'], ['g']])])
  <tf.RaggedTensor [[b'a_X_d_X_f'], [b'b_X_e_X_g', b'c_X_e_X_g']]>

  Args:
    inputs: A list of `RaggedTensor` or `Tensor` or `SparseTensor`.
    name: Optional name for the op.

  Returns:
    A 2D `RaggedTensor` of type `string`.
  """
exit(_cross_internal(inputs=inputs, hashed_output=False, name=name))
