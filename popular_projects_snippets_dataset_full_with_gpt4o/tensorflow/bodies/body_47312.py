# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend_config.py
"""Sets the value of the fuzz factor used in numeric expressions.

  Args:
      value: float. New value of epsilon.

  Example:
  >>> tf.keras.backend.epsilon()
  1e-07
  >>> tf.keras.backend.set_epsilon(1e-5)
  >>> tf.keras.backend.epsilon()
  1e-05
   >>> tf.keras.backend.set_epsilon(1e-7)
  """
global _EPSILON
_EPSILON = value
