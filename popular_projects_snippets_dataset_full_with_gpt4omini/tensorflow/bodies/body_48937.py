# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Retrieves the output shape(s) of a layer.

    Only applicable if the layer has one output,
    or if all outputs have the same shape.

    Returns:
        Output shape, as an integer shape tuple
        (or list of shape tuples, one tuple per output tensor).

    Raises:
        AttributeError: if the layer has no defined output shape.
        RuntimeError: if called in Eager mode.
    """
if not self._inbound_nodes:
    raise AttributeError('The layer has never been called '
                         'and thus has no defined output shape.')
all_output_shapes = set(
    [str(node.output_shapes) for node in self._inbound_nodes])
if len(all_output_shapes) == 1:
    exit(self._inbound_nodes[0].output_shapes)
else:
    raise AttributeError('The layer "%s"'
                         ' has multiple inbound nodes, '
                         'with different output shapes. Hence '
                         'the notion of "output shape" is '
                         'ill-defined for the layer. '
                         'Use `get_output_shape_at(node_index)` '
                         'instead.' % self.name)
