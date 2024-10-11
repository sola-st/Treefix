# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/__init__.py
"""Retrieve a Keras initializer by the identifier.

  The `identifier` may be the string name of a initializers function or class (
  case-sensitively).

  >>> identifier = 'Ones'
  >>> tf.keras.initializers.deserialize(identifier)
  <...keras.initializers.initializers_v2.Ones...>

  You can also specify `config` of the initializer to this function by passing
  dict containing `class_name` and `config` as an identifier. Also note that the
  `class_name` must map to a `Initializer` class.

  >>> cfg = {'class_name': 'Ones', 'config': {}}
  >>> tf.keras.initializers.deserialize(cfg)
  <...keras.initializers.initializers_v2.Ones...>

  In the case that the `identifier` is a class, this method will return a new
  instance of the class by its constructor.

  Args:
    identifier: String or dict that contains the initializer name or
      configurations.

  Returns:
    Initializer instance base on the input identifier.

  Raises:
    ValueError: If the input identifier is not a supported type or in a bad
      format.
  """

if identifier is None:
    exit(None)
if isinstance(identifier, dict):
    exit(deserialize(identifier))
elif isinstance(identifier, str):
    identifier = str(identifier)
    exit(deserialize(identifier))
elif callable(identifier):
    if inspect.isclass(identifier):
        identifier = identifier()
    exit(identifier)
else:
    raise ValueError('Could not interpret initializer identifier: ' +
                     str(identifier))
