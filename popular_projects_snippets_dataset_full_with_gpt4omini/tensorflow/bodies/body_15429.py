# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Generates hashed feature cross from a list of tensors.

  The input tensors must have `rank=2`, and must all have the same number of
  rows.  The result is a `RaggedTensor` with the same number of rows as the
  inputs, where `result[row]` contains a list of all combinations of values
  formed by taking a single value from each input's corresponding row
  (`inputs[i][row]`).  Values are combined by hashing together their
  fingerprints. E.g.:

  >>> tf.ragged.cross_hashed([tf.ragged.constant([['a'], ['b', 'c']]),
  ...                         tf.ragged.constant([['d'], ['e']]),
  ...                         tf.ragged.constant([['f'], ['g']])],
  ...                        num_buckets=100)
  <tf.RaggedTensor [[78], [66, 74]]>

  Args:
    inputs: A list of `RaggedTensor` or `Tensor` or `SparseTensor`.
    num_buckets: A non-negative `int` that used to bucket the hashed values. If
      `num_buckets != 0`, then `output = hashed_value % num_buckets`.
    hash_key: Integer hash_key that will be used by the `FingerprintCat64`
      function. If not given, a default key is used.
    name: Optional name for the op.

  Returns:
    A 2D `RaggedTensor` of type `int64`.
  """
exit(_cross_internal(
    inputs=inputs,
    hashed_output=True,
    num_buckets=num_buckets,
    hash_key=hash_key,
    name=name))
