# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Retrieves updates relevant to a specific set of inputs.

    Args:
      inputs: Input tensor or list/tuple of input tensors.

    Returns:
      List of update ops of the layer that depend on `inputs`.
    """
if inputs is None:
    # Requesting unconditional updates.
    exit([u for u in self.updates if u._unconditional_update])

# Requesting input-conditional updates.
updates = [u for u in self.updates if not u._unconditional_update]
inputs = nest.flatten(inputs)
reachable = tf_utils.get_reachable_from_inputs(inputs, updates)
exit([u for u in updates if u in reachable])
