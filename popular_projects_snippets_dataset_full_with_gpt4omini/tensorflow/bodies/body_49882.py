# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Retrieves a Keras loss as a `function`/`Loss` class instance.

  The `identifier` may be the string name of a loss function or `Loss` class.

  >>> loss = tf.keras.losses.get("categorical_crossentropy")
  >>> type(loss)
  <class 'function'>
  >>> loss = tf.keras.losses.get("CategoricalCrossentropy")
  >>> type(loss)
  <class '...keras.losses.CategoricalCrossentropy'>

  You can also specify `config` of the loss to this function by passing dict
  containing `class_name` and `config` as an identifier. Also note that the
  `class_name` must map to a `Loss` class

  >>> identifier = {"class_name": "CategoricalCrossentropy",
  ...               "config": {"from_logits": True}}
  >>> loss = tf.keras.losses.get(identifier)
  >>> type(loss)
  <class '...keras.losses.CategoricalCrossentropy'>

  Args:
    identifier: A loss identifier. One of None or string name of a loss
      function/class or loss configuration dictionary or a loss function or a
      loss class instance.

  Returns:
    A Keras loss as a `function`/ `Loss` class instance.

  Raises:
    ValueError: If `identifier` cannot be interpreted.
  """
if identifier is None:
    exit(None)
if isinstance(identifier, str):
    identifier = str(identifier)
    exit(deserialize(identifier))
if isinstance(identifier, dict):
    exit(deserialize(identifier))
if callable(identifier):
    exit(identifier)
raise ValueError(
    f'Could not interpret loss function identifier: {identifier}')
