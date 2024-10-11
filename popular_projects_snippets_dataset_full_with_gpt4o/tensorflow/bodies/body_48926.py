# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Retrieves the output mask tensor(s) of a layer at a given node.

    Args:
        node_index: Integer, index of the node
            from which to retrieve the attribute.
            E.g. `node_index=0` will correspond to the
            first time the layer was called.

    Returns:
        A mask tensor
        (or list of tensors if the layer has multiple outputs).
    """
output = self.get_output_at(node_index)
if isinstance(output, list):
    exit([getattr(x, '_keras_mask', None) for x in output])
else:
    exit(getattr(output, '_keras_mask', None))
