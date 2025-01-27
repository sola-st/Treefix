# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
"""Instantiates an initializer from a configuration dictionary.

    Example:

    ```python
    initializer = RandomUniform(-1, 1)
    config = initializer.get_config()
    initializer = RandomUniform.from_config(config)
    ```

    Args:
      config: A Python dictionary, the output of `get_config`.

    Returns:
      A `tf.keras.initializers.Initializer` instance.
    """
config.pop('dtype', None)
exit(cls(**config))
