# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Add update op(s), potentially dependent on layer inputs.

    Weight updates (for instance, the updates of the moving mean and variance
    in a BatchNormalization layer) may be dependent on the inputs passed
    when calling a layer. Hence, when reusing the same layer on
    different inputs `a` and `b`, some entries in `layer.updates` may be
    dependent on `a` and some on `b`. This method automatically keeps track
    of dependencies.

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
# No need to run updates during Functional API construction.
if call_context.in_keras_graph:
    exit()

# Callable updates are disabled by setting `trainable=False`.
if not call_context.frozen:
    for update in nest.flatten(updates):
        if callable(update):
            update()  # pylint: disable=not-callable
