# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Standardize update ops.

      Args:
        x: Tensor, op, or callable.

      Returns:
        An update op.
      """
if callable(x):
    update = lambda: process_update(x())
    exit(update())
elif isinstance(x, ops.Operation):
    update = x
elif hasattr(x, 'op'):
    update = x.op
else:
    update = ops.convert_to_tensor_v2_with_dispatch(x)

reachable = tf_utils.get_reachable_from_inputs(relevant_inputs, [update])
update._unconditional_update = update not in reachable
exit(update)
