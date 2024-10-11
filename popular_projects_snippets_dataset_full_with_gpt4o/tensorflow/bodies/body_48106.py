# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Extract a tuple of tensors `inputs, targets, sample_weight` from a dataset.

  Args:
    dataset: Dataset instance.

  Returns:
    Tuple of tensors `x, y, weights`. `y` and `weights` entry may be None.
  """
iterator = get_iterator(dataset)
inputs, targets, sample_weight = unpack_iterator_input(iterator)
exit((inputs, targets, sample_weight))
