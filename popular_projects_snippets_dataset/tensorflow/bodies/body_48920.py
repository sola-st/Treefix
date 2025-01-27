# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Sets the weights of the layer, from NumPy arrays.

    The weights of a layer represent the state of the layer. This function
    sets the weight values from numpy arrays. The weight values should be
    passed in the order they are created by the layer. Note that the layer's
    weights must be instantiated before calling this function, by calling
    the layer.

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

    Args:
      weights: a list of NumPy arrays. The number
        of arrays and their shape must match
        number of the dimensions of the weights
        of the layer (i.e. it should match the
        output of `get_weights`).

    Raises:
      ValueError: If the provided weights list does not match the
        layer's specifications.
    """
params = self.weights

expected_num_weights = 0
for param in params:
    if isinstance(param, base_layer_utils.TrackableWeightHandler):
        expected_num_weights += param.num_tensors
    else:
        expected_num_weights += 1

if expected_num_weights != len(weights):
    raise ValueError(
        'You called `set_weights(weights)` on layer "%s" '
        'with a weight list of length %s, but the layer was '
        'expecting %s weights. Provided weights: %s...' %
        (self.name, len(weights), expected_num_weights, str(weights)[:50]))

weight_index = 0
weight_value_tuples = []
for param in params:
    if isinstance(param, base_layer_utils.TrackableWeightHandler):
        num_tensors = param.num_tensors
        tensors = weights[weight_index:weight_index + num_tensors]
        param.set_weights(tensors)
        weight_index += num_tensors
    else:
        weight = weights[weight_index]
        weight_shape = weight.shape if hasattr(weight, 'shape') else ()
        ref_shape = param.shape
        if not ref_shape.is_compatible_with(weight_shape):
            raise ValueError(
                'Layer weight shape %s not compatible with provided weight '
                'shape %s' % (ref_shape, weight_shape))
        weight_value_tuples.append((param, weight))
        weight_index += 1

backend.batch_set_value(weight_value_tuples)

# Perform any layer defined finalization of the layer state.
for layer in self._flatten_layers():
    layer.finalize_state()
