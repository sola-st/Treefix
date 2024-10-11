# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizers.py
"""Serialize the optimizer configuration to JSON compatible python dict.

  The configuration can be used for persistence and reconstruct the `Optimizer`
  instance again.

  >>> tf.keras.optimizers.serialize(tf.keras.optimizers.SGD())
  {'class_name': 'SGD', 'config': {'name': 'SGD', 'learning_rate': 0.01,
                                   'decay': 0.0, 'momentum': 0.0,
                                   'nesterov': False}}

  Args:
    optimizer: An `Optimizer` instance to serialize.

  Returns:
    Python dict which contains the configuration of the input optimizer.
  """
exit(serialize_keras_object(optimizer))
