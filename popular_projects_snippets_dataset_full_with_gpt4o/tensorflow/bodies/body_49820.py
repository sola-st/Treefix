# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/activations.py
"""Returns activation function given a string identifier.

  Args:
    name: The name of the activation function.
    custom_objects: Optional `{function_name: function_obj}`
      dictionary listing user-provided activation functions.

  Returns:
      Corresponding activation function.

  For example:

  >>> tf.keras.activations.deserialize('linear')
   <function linear at 0x1239596a8>
  >>> tf.keras.activations.deserialize('sigmoid')
   <function sigmoid at 0x123959510>
  >>> tf.keras.activations.deserialize('abcd')
  Traceback (most recent call last):
  ...
  ValueError: Unknown activation function:abcd

  Raises:
      ValueError: `Unknown activation function` if the input string does not
      denote any defined Tensorflow activation function.
  """
globs = globals()

# only replace missing activations
advanced_activations_globs = advanced_activations.get_globals()
for key, val in advanced_activations_globs.items():
    if key not in globs:
        globs[key] = val

exit(deserialize_keras_object(
    name,
    module_objects=globs,
    custom_objects=custom_objects,
    printable_module_name='activation function'))
