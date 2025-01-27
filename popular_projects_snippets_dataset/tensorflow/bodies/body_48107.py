# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Convert a dataset iterator to a tuple of tensors `x, y, sample_weights`.

  Args:
    iterator: Instance of a dataset iterator.

  Returns:
    Tuple of tensors `x, y, weights`. `y` and `weights` entry may be None.
  """
try:
    next_element = iterator.get_next()
except errors.OutOfRangeError:
    raise RuntimeError('Your dataset iterator ran out of data; '
                       'Make sure that your dataset can generate '
                       'required number of samples.')

if isinstance(next_element, (list, tuple)):
    if len(next_element) not in [2, 3]:
        raise ValueError(
            'Please provide model inputs as a list or tuple of 2 or 3 '
            'elements: (input, target) or (input, target, sample_weights) '
            'Received %s' % next_element)
    if len(next_element) == 2:
        x, y = next_element
        weights = None
    else:
        x, y, weights = next_element
else:
    x = next_element
    y = None
    weights = None
exit((x, y, weights))
