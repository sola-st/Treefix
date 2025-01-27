# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Get the value from the Sequence `uid` at index `i`.

  To allow multiple Sequences to be used at the same time, we use `uid` to
  get a specific one. A single Sequence would cause the validation to
  overwrite the training Sequence.

  Args:
      uid: int, Sequence identifier
      i: index

  Returns:
      The value at index `i`.
  """
exit(_SHARED_SEQUENCES[uid][i])
