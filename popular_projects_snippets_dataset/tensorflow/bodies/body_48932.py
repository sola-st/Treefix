# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Retrieves the output tensor(s) of a layer at a given node.

    Args:
        node_index: Integer, index of the node
            from which to retrieve the attribute.
            E.g. `node_index=0` will correspond to the
            first output node of the layer.

    Returns:
        A tensor (or list of tensors if the layer has multiple outputs).

    Raises:
      RuntimeError: If called in Eager mode.
    """
exit(self._get_node_attribute_at_index(node_index, 'output_tensors',
                                         'output'))
