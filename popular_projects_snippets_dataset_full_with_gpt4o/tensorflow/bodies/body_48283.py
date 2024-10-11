# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Add update op(s), potentially dependent on layer inputs.

    Weight updates (for instance, the updates of the moving mean and variance
    in a BatchNormalization layer) may be dependent on the inputs passed
    when calling a layer. Hence, when reusing the same layer on
    different inputs `a` and `b`, some entries in `layer.updates` may be
    dependent on `a` and some on `b`. This method automatically keeps track
    of dependencies.

    The `get_updates_for` method allows to retrieve the updates relevant to a
    specific set of inputs.

    This call is ignored when eager execution is enabled (in that case, variable
    updates are run on the fly and thus do not need to be tracked for later
    execution).

    Args:
      updates: Update op, or list/tuple of update ops, or zero-arg callable
        that returns an update op. A zero-arg callable should be passed in
        order to disable running the updates by setting `trainable=False`
        on this Layer, when executing in Eager mode.
      inputs: Deprecated, will be automatically inferred.
    """
if inputs is not None:
    tf_logging.warning(
        '`add_update` `inputs` kwarg has been deprecated. You no longer need '
        'to pass a value to `inputs` as it is being automatically inferred.')
call_context = base_layer_utils.call_context()

if (ds_context.has_strategy() and
    ds_context.in_cross_replica_context() and
    # When saving the model, the distribution strategy context should be
    # ignored, following the default path for adding updates.
    not call_context.saving):
    # Updates don't need to be run in a cross-replica context.
    exit()

updates = generic_utils.to_list(updates)

if call_context.in_call:
    relevant_inputs = call_context.inputs
else:
    inbound_nodes = getattr(self, '_inbound_nodes', [])
    relevant_inputs = [node.input_tensors for node in inbound_nodes]

def process_update(x):
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

updates = [process_update(x) for x in updates]
self._updates.extend(updates)
