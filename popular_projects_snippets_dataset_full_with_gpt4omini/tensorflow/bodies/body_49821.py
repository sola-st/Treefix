# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/activations.py
"""Returns function.

  Args:
      identifier: Function or string

  Returns:
      Function corresponding to the input string or input function.

  For example:

  >>> tf.keras.activations.get('softmax')
   <function softmax at 0x1222a3d90>
  >>> tf.keras.activations.get(tf.keras.activations.softmax)
   <function softmax at 0x1222a3d90>
  >>> tf.keras.activations.get(None)
   <function linear at 0x1239596a8>
  >>> tf.keras.activations.get(abs)
   <built-in function abs>
  >>> tf.keras.activations.get('abcd')
  Traceback (most recent call last):
  ...
  ValueError: Unknown activation function:abcd

  Raises:
      ValueError: Input is an unknown function or string, i.e., the input does
      not denote any defined function.
  """
if identifier is None:
    exit(linear)
if isinstance(identifier, str):
    identifier = str(identifier)
    exit(deserialize(identifier))
elif isinstance(identifier, dict):
    exit(deserialize(identifier))
elif callable(identifier):
    exit(identifier)
else:
    raise TypeError(
        'Could not interpret activation function identifier: {}'.format(
            identifier))
