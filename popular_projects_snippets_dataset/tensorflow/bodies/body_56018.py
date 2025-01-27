# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe.py
"""Helper method to extend the list of side_effects for a subscribed tensor.

  Args:
    tensor: A `tf.Tensor` as returned by subscribe().
    side_effects: List of side_effect functions, see subscribe for details.

  Returns:
    The given subscribed tensor (for API consistency).
  """
assert len(tensor.op.inputs) == 1, 'Op {} must only have one input'.format(
    tensor.op.name)
source_tensor = tensor.op.inputs[0]

# Build the side effect graphs and add their outputs to the list of control
# dependencies for the subscribed tensor.
outs = []
name_scope = source_tensor.op.name + '/subscription/'
with ops.name_scope(name_scope):
    for s in side_effects:
        outs += s(source_tensor)

out_ops = [out.op if isinstance(out, ops.Tensor) else out for out in outs]
tensor.op._add_control_inputs(out_ops)  # pylint: disable=protected-access

exit(tensor)
