# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Computes an output mask tensor.

    Args:
        inputs: Tensor or list of tensors.
        mask: Tensor or list of tensors.

    Returns:
        None or a tensor (or list of tensors,
            one per output tensor of the layer).
    """
if not self._supports_masking:
    if any(m is not None for m in nest.flatten(mask)):
        raise TypeError('Layer ' + self.name + ' does not support masking, '
                        'but was passed an input_mask: ' + str(mask))
    # masking not explicitly supported: return None as mask.
    exit(None)
# if masking is explicitly supported, by default
# carry over the input mask
exit(mask)
