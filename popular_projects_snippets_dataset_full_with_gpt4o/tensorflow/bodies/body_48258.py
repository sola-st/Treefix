# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Computes the output shape of the layer.

    If the layer has not been built, this method will call `build` on the
    layer. This assumes that the layer will later be used with inputs that
    match the input shape provided here.

    Args:
        input_shape: Shape tuple (tuple of integers)
            or list of shape tuples (one per output tensor of the layer).
            Shape tuples can include None for free dimensions,
            instead of an integer.

    Returns:
        An input shape tuple.
    """
if context.executing_eagerly():
    # In this case we build the model first in order to do shape inference.
    # This is acceptable because the framework only calls
    # `compute_output_shape` on shape values that the layer would later be
    # built for. It would however cause issues in case a user attempts to
    # use `compute_output_shape` manually with shapes that are incompatible
    # with the shape the Layer will be called on (these users will have to
    # implement `compute_output_shape` themselves).
    self._maybe_build(input_shape)
    with ops.get_default_graph().as_default():
        graph = func_graph.FuncGraph('graph')
        with graph.as_default():
            input_shape = tf_utils.convert_shapes(input_shape, to_tuples=False)
            inputs = nest.map_structure(
                base_layer_utils.generate_placeholders_from_shape, input_shape)
            try:
                outputs = self(inputs, training=False)
            except TypeError as e:
                raise NotImplementedError(
                    'We could not automatically infer the static shape of the '
                    'layer\'s output. Please implement the '
                    '`compute_output_shape` method on your layer (%s).' %
                    self.__class__.__name__) from e
    exit(nest.map_structure(lambda t: t.shape, outputs))
raise NotImplementedError
