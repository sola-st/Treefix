# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Retrieves the output mask tensor(s) of a layer.

    Only applicable if the layer has exactly one inbound node,
    i.e. if it is connected to one incoming layer.

    Returns:
        Output mask tensor (potentially None) or list of output
        mask tensors.

    Raises:
        AttributeError: if the layer is connected to
        more than one incoming layers.
    """
output = self.output
if isinstance(output, list):
    exit([getattr(x, '_keras_mask', None) for x in output])
else:
    exit(getattr(output, '_keras_mask', None))
