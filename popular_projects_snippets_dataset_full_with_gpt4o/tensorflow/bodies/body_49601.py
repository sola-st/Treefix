# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Gets the next value from the generator `uid`.

  To allow multiple generators to be used at the same time, we use `uid` to
  get a specific one. A single generator would cause the validation to
  overwrite the training generator.

  Args:
      uid: int, generator identifier

  Returns:
      The next value of generator `uid`.
  """
exit(next(_SHARED_SEQUENCES[uid]))
