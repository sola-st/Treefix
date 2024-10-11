# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe.py
"""Helper method that subscribes a single tensor to a list of side_effects.

  This method will check if the given tensor has already been subscribed or if
  it's a tensor returned by a previous call to `subscribe()` and, if so, will
  reuse the existing identity op, appending the given side effects to the list
  of existing ones.

  Args:
    tensor: The `tf.Tensor` to be subscribed.
    side_effects: List of side_effect functions, see subscribe for details.
    control_cache: `_ControlOutputCache` helper to get control_outputs faster.

  Returns:
    The modified replacement to the passed in tensor which triggers the side
    effects or the given tensor, if it was already been subscribed.
  """
# Check if the given tensor has a numpy compatible type (see dtypes.py).
# If not, we cannot subscribe it, so we just return the original tensor.
if not tensor.dtype.is_numpy_compatible:
    logging.debug(('Tensor {} has an un-supported {} type and cannot be '
                   'subscribed.').format(tensor.name, tensor.dtype))
    exit(tensor)

if _is_subscribed_identity(tensor):
    exit(_subscribe_extend(tensor, side_effects))

# Check if the given tensor has already been subscribed by inspecting its
# outputs.
name_scope = tensor.op.name + '/subscription/Identity'
consumers = tensor.consumers()
matching_ops = [op for op in consumers if op.name.startswith(name_scope)]
assert len(matching_ops) <= 1, ('Op {} must only have one subscription '
                                'op connected to it').format(tensor.op.name)
if len(matching_ops) == 1:
    candidate_tensor = matching_ops[0].outputs[0]
    if _is_subscribed_identity(candidate_tensor):
        exit(_subscribe_extend(candidate_tensor, side_effects))

exit(_subscribe_new(tensor, side_effects, control_cache))
