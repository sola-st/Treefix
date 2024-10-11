# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Validates user input arguments when a dataset iterator is passed.

  Args:
    x: Input data. A `tf.data` dataset or iterator.
    y: Target data. It could be either Numpy array(s) or TensorFlow tensor(s).
      Expected to be `None` when `x` is a dataset iterator.
    sample_weight: An optional sample-weight array passed by the user to weight
      the importance of each sample in `x`. Expected to be `None` when `x` is a
      dataset iterator
    validation_split: Float between 0 and 1. Fraction of the training data to be
      used as validation data. Expected to be `None` when `x` is a dataset
      iterator.

  Raises:
    ValueError: if argument `y` or `sample_weight` or `validation_split` are
        provided by user.
  """
if y is not None:
    raise ValueError('You passed a dataset or dataset iterator (%s) as '
                     'input `x` to your model. In that case, you should '
                     'not specify a target (`y`) argument, since the dataset '
                     'or dataset iterator generates both input data and '
                     'target data. '
                     'Received: %s' % (x, y))
if sample_weight is not None:
    raise ValueError('`sample_weight` argument is not supported when input '
                     '`x` is a dataset or a dataset iterator. Instead, you'
                     'can provide sample_weight as the third element  of your'
                     'dataset, i.e. (inputs, targets, sample_weight). '
                     'Received: x=%s, sample_weight=%s' % (x, sample_weight))
if validation_split is not None and validation_split != 0.0:
    raise ValueError(
        '`validation_split` argument is not supported when '
        'input `x` is a dataset or a dataset iterator. '
        'Received: x=%s, validation_split=%f' % (x, validation_split))
