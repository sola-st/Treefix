# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Returns the current weights of the layer, as NumPy arrays.

    The weights of a layer represent the state of the layer. This function
    returns both trainable and non-trainable weight values associated with this
    layer as a list of NumPy arrays, which can in turn be used to load state
    into similarly parameterized layers.

    For example, a `Dense` layer returns a list of two values: the kernel matrix
    and the bias vector. These can be used to set the weights of another
    `Dense` layer:

    >>> layer_a = tf.keras.layers.Dense(1,
    ...   kernel_initializer=tf.constant_initializer(1.))
    >>> a_out = layer_a(tf.convert_to_tensor([[1., 2., 3.]]))
    >>> layer_a.get_weights()
    [array([[1.],
           [1.],
           [1.]], dtype=float32), array([0.], dtype=float32)]
    >>> layer_b = tf.keras.layers.Dense(1,
    ...   kernel_initializer=tf.constant_initializer(2.))
    >>> b_out = layer_b(tf.convert_to_tensor([[10., 20., 30.]]))
    >>> layer_b.get_weights()
    [array([[2.],
           [2.],
           [2.]], dtype=float32), array([0.], dtype=float32)]
    >>> layer_b.set_weights(layer_a.get_weights())
    >>> layer_b.get_weights()
    [array([[1.],
           [1.],
           [1.]], dtype=float32), array([0.], dtype=float32)]

    Returns:
        Weights values as a list of NumPy arrays.
    """
weights = self.weights
output_weights = []
for weight in weights:
    if isinstance(weight, base_layer_utils.TrackableWeightHandler):
        output_weights.extend(weight.get_tensors())
    else:
        output_weights.append(weight)
exit(backend.batch_get_value(output_weights))
