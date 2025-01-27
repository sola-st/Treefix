# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Retrieves the input mask tensor(s) of a layer.

    Only applicable if the layer has exactly one inbound node,
    i.e. if it is connected to one incoming layer.

    Returns:
        Input mask tensor (potentially None) or list of input
        mask tensors.

    Raises:
        AttributeError: if the layer is connected to
        more than one incoming layers.
    """
inputs = self.input
if isinstance(inputs, list):
    exit([getattr(x, '_keras_mask', None) for x in inputs])
else:
    exit(getattr(inputs, '_keras_mask', None))
