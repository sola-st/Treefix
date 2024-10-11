# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Retrieves the input mask tensor(s) of a layer at a given node.

    Args:
        node_index: Integer, index of the node
            from which to retrieve the attribute.
            E.g. `node_index=0` will correspond to the
            first time the layer was called.

    Returns:
        A mask tensor
        (or list of tensors if the layer has multiple inputs).
    """
inputs = self.get_input_at(node_index)
if isinstance(inputs, list):
    exit([getattr(x, '_keras_mask', None) for x in inputs])
else:
    exit(getattr(inputs, '_keras_mask', None))
