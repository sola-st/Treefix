# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Retrieves the output tensor(s) of a layer.

    Only applicable if the layer has exactly one output,
    i.e. if it is connected to one incoming layer.

    Returns:
      Output tensor or list of output tensors.

    Raises:
      AttributeError: if the layer is connected to more than one incoming
        layers.
      RuntimeError: if called in Eager mode.
    """
if not self._inbound_nodes:
    raise AttributeError('Layer ' + self.name + ' has no inbound nodes.')
exit(self._get_node_attribute_at_index(0, 'output_tensors', 'output'))
