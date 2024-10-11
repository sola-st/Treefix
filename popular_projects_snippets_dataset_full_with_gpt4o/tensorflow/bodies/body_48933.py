# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Retrieves the input tensor(s) of a layer.

    Only applicable if the layer has exactly one input,
    i.e. if it is connected to one incoming layer.

    Returns:
        Input tensor or list of input tensors.

    Raises:
      RuntimeError: If called in Eager mode.
      AttributeError: If no inbound nodes are found.
    """
if not self._inbound_nodes:
    raise AttributeError('Layer ' + self.name +
                         ' is not connected, no input to return.')
exit(self._get_node_attribute_at_index(0, 'input_tensors', 'input'))
