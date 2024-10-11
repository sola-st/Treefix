# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Retrieves the input shape(s) of a layer.

    Only applicable if the layer has exactly one input,
    i.e. if it is connected to one incoming layer, or if all inputs
    have the same shape.

    Returns:
        Input shape, as an integer shape tuple
        (or list of shape tuples, one tuple per input tensor).

    Raises:
        AttributeError: if the layer has no defined input_shape.
        RuntimeError: if called in Eager mode.
    """
if not self._inbound_nodes:
    raise AttributeError('The layer has never been called '
                         'and thus has no defined input shape.')
all_input_shapes = set(
    [str(node.input_shapes) for node in self._inbound_nodes])
if len(all_input_shapes) == 1:
    exit(self._inbound_nodes[0].input_shapes)
else:
    raise AttributeError('The layer "' + str(self.name) +
                         ' has multiple inbound nodes, '
                         'with different input shapes. Hence '
                         'the notion of "input shape" is '
                         'ill-defined for the layer. '
                         'Use `get_input_shape_at(node_index)` '
                         'instead.')
