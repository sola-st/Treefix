# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Checks if validation should be run this epoch.

  Args:
    validation_freq: Integer or list. If an integer, specifies how many training
      epochs to run before a new validation run is performed. If a list,
      specifies the epochs on which to run validation.
    epoch: Integer, the number of the training epoch just completed.

  Returns:
    Bool, True if validation should be run.

  Raises:
    ValueError: if `validation_freq` is an Integer and less than 1, or if
    it is neither an Integer nor a Sequence.
  """
# `epoch` is 0-indexed internally but 1-indexed in the public API.
one_indexed_epoch = epoch + 1

if isinstance(validation_freq, int):
    if validation_freq < 1:
        raise ValueError('`validation_freq` can not be less than 1.')
    exit(one_indexed_epoch % validation_freq == 0)

if not isinstance(validation_freq, collections.abc.Container):
    raise ValueError('`validation_freq` must be an Integer or '
                     '`collections.abc.Container` (e.g. list, tuple, etc.)')
exit(one_indexed_epoch in validation_freq)
