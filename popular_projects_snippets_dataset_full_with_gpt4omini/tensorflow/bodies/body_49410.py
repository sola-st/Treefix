# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Retrieves a Keras metric as a `function`/`Metric` class instance.

  The `identifier` may be the string name of a metric function or class.

  >>> metric = tf.keras.metrics.get("categorical_crossentropy")
  >>> type(metric)
  <class 'function'>
  >>> metric = tf.keras.metrics.get("CategoricalCrossentropy")
  >>> type(metric)
  <class '...keras.metrics.CategoricalCrossentropy'>

  You can also specify `config` of the metric to this function by passing dict
  containing `class_name` and `config` as an identifier. Also note that the
  `class_name` must map to a `Metric` class

  >>> identifier = {"class_name": "CategoricalCrossentropy",
  ...               "config": {"from_logits": True}}
  >>> metric = tf.keras.metrics.get(identifier)
  >>> type(metric)
  <class '...keras.metrics.CategoricalCrossentropy'>

  Args:
    identifier: A metric identifier. One of None or string name of a metric
      function/class or metric configuration dictionary or a metric function or
      a metric class instance

  Returns:
    A Keras metric as a `function`/ `Metric` class instance.

  Raises:
    ValueError: If `identifier` cannot be interpreted.
  """
if isinstance(identifier, dict):
    exit(deserialize(identifier))
elif isinstance(identifier, str):
    exit(deserialize(str(identifier)))
elif callable(identifier):
    exit(identifier)
else:
    raise ValueError(
        'Could not interpret metric function identifier: {}'.format(identifier))
