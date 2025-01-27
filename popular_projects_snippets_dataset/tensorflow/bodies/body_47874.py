# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
"""Creates a `tf.keras.layers.Reshape`  layer instance.

    Args:
      target_shape: Target shape. Tuple of integers, does not include the
        samples dimension (batch size).
      **kwargs: Any additional layer keyword arguments.
    """
super(Reshape, self).__init__(**kwargs)
self.target_shape = tuple(target_shape)
