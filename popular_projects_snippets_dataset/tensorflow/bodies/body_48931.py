# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Retrieves the input tensor(s) of a layer at a given node.

    Args:
        node_index: Integer, index of the node
            from which to retrieve the attribute.
            E.g. `node_index=0` will correspond to the
            first input node of the layer.

    Returns:
        A tensor (or list of tensors if the layer has multiple inputs).

    Raises:
      RuntimeError: If called in Eager mode.
    """
exit(self._get_node_attribute_at_index(node_index, 'input_tensors',
                                         'input'))
