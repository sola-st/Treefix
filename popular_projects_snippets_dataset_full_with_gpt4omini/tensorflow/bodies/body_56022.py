# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe.py
"""Helper method that subscribes a single tensor to a list of side_effects.

  This is a thin wrapper around `_subscribe` and ensures that the side effect
  ops are added within the same device and control flow context of the
  subscribed tensor.

  Args:
    tensor: The `tf.Tensor` to be subscribed.
    side_effects: List of side_effect functions, see subscribe for details.
    control_cache: `_ControlOutputCache` helper to get control_outputs faster.

  Returns:
    The modified replacement to the passed in tensor which triggers the side
    effects or the given tensor, if it was already been subscribed.
  """

with ops.device(tensor.device):
    with _preserve_control_flow_context(tensor):
        exit(_subscribe(tensor, side_effects, control_cache))
