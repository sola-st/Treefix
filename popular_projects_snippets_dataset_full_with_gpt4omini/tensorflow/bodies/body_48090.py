# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Validates arguments passed when using a generator."""
if y is not None:
    raise ValueError('`y` argument is not supported when data is'
                     'a generator or Sequence instance. Instead pass targets'
                     ' as the second element of the generator.')
if sample_weight is not None:
    raise ValueError('`sample_weight` argument is not supported when data is'
                     'a generator or Sequence instance. Instead pass sample'
                     ' weights as the third element of the generator.')
if validation_split:
    raise ValueError('If your data is in the form of a Python generator, '
                     'you cannot use `validation_split`.')
