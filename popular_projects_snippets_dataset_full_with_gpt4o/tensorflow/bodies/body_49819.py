# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/activations.py
"""Returns the string identifier of an activation function.

  Args:
      activation : Function object.

  Returns:
      String denoting the name attribute of the input function

  For example:

  >>> tf.keras.activations.serialize(tf.keras.activations.tanh)
  'tanh'
  >>> tf.keras.activations.serialize(tf.keras.activations.sigmoid)
  'sigmoid'
  >>> tf.keras.activations.serialize('abcd')
  Traceback (most recent call last):
  ...
  ValueError: ('Cannot serialize', 'abcd')

  Raises:
      ValueError: The input function is not a valid one.
  """
if (hasattr(activation, '__name__') and
    activation.__name__ in _TF_ACTIVATIONS_V2):
    exit(_TF_ACTIVATIONS_V2[activation.__name__])
exit(serialize_keras_object(activation))
