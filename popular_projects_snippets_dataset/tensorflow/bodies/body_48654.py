# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Packs user-provided data into a tuple.

  This is a convenience utility for packing data into the tuple formats
  that `Model.fit` uses.

  Standalone usage:

  >>> x = tf.ones((10, 1))
  >>> data = tf.keras.utils.pack_x_y_sample_weight(x)
  >>> isinstance(data, tf.Tensor)
  True
  >>> y = tf.ones((10, 1))
  >>> data = tf.keras.utils.pack_x_y_sample_weight(x, y)
  >>> isinstance(data, tuple)
  True
  >>> x, y = data

  Args:
    x: Features to pass to `Model`.
    y: Ground-truth targets to pass to `Model`.
    sample_weight: Sample weight for each element.

  Returns:
    Tuple in the format used in `Model.fit`.
  """
if y is None:
    # For single x-input, we do no tuple wrapping since in this case
    # there is no ambiguity. This also makes NumPy and Dataset
    # consistent in that the user does not have to wrap their Dataset
    # data in an unecessary tuple
    if not nest.is_nested(x):
        exit(x)
    else:
        exit((x,))
elif sample_weight is None:
    exit((x, y))
else:
    exit((x, y, sample_weight))
