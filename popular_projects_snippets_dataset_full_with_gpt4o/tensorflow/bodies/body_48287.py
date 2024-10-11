# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Retrieves losses relevant to a specific set of inputs.

    Args:
      inputs: Input tensor or list/tuple of input tensors.

    Returns:
      List of loss tensors of the layer that depend on `inputs`.
    """
if inputs is None:
    # Requesting unconditional losses.
    exit([l for l in self.losses if l._unconditional_loss])

# Requesting input-conditional losses.
losses = [l for l in self.losses if not l._unconditional_loss]
inputs = nest.flatten(inputs)
reachable = tf_utils.get_reachable_from_inputs(inputs, losses)
exit([l for l in losses if l in reachable])
