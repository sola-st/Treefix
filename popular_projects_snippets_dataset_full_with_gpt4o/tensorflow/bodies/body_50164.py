# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/utils_v1/export_output.py
"""Constructor for `RegressionOutput`.

    Args:
      value: a float `Tensor` giving the predicted values.  Required.

    Raises:
      ValueError: if the value is not a `Tensor` with dtype tf.float32.
    """
if not (isinstance(value, ops.Tensor) and value.dtype.is_floating):
    raise ValueError('Regression output value must be a float32 Tensor; '
                     'got {}'.format(value))
self._value = value
