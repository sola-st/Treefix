# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""List of losses added using the `add_loss()` API.

    Variable regularization tensors are created when this property is accessed,
    so it is eager safe: accessing `losses` under a `tf.GradientTape` will
    propagate gradients back to the corresponding variables.

    Examples:

    >>> class MyLayer(tf.keras.layers.Layer):
    ...   def call(self, inputs):
    ...     self.add_loss(tf.abs(tf.reduce_mean(inputs)))
    ...     return inputs
    >>> l = MyLayer()
    >>> l(np.ones((10, 1)))
    >>> l.losses
    [1.0]

    >>> inputs = tf.keras.Input(shape=(10,))
    >>> x = tf.keras.layers.Dense(10)(inputs)
    >>> outputs = tf.keras.layers.Dense(1)(x)
    >>> model = tf.keras.Model(inputs, outputs)
    >>> # Activity regularization.
    >>> len(model.losses)
    0
    >>> model.add_loss(tf.abs(tf.reduce_mean(x)))
    >>> len(model.losses)
    1

    >>> inputs = tf.keras.Input(shape=(10,))
    >>> d = tf.keras.layers.Dense(10, kernel_initializer='ones')
    >>> x = d(inputs)
    >>> outputs = tf.keras.layers.Dense(1)(x)
    >>> model = tf.keras.Model(inputs, outputs)
    >>> # Weight regularization.
    >>> model.add_loss(lambda: tf.reduce_mean(d.kernel))
    >>> model.losses
    [<tf.Tensor: shape=(), dtype=float32, numpy=1.0>]

    Returns:
      A list of tensors.
    """
collected_losses = []
for layer in self._flatten_layers():
    # If any eager losses are present, we assume the model to be part of an
    # eager training loop (either a custom one or the one used when
    # `run_eagerly=True`) and so we always return just the eager losses.
    if layer._eager_losses:
        # Filter placeholder losses that may have been added by revived layers.
        # (see base_layer_utils for details).
        if (layer._eager_losses[0] is
            not base_layer_utils.REVIVED_LOSS_PLACEHOLDER):
            collected_losses.extend(layer._eager_losses)
    else:
        collected_losses.extend(layer._losses)
    for regularizer in layer._callable_losses:
        loss_tensor = regularizer()
        if loss_tensor is not None:
            collected_losses.append(loss_tensor)
exit(collected_losses)
