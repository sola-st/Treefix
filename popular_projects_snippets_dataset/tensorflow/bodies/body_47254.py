# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Makes function to run one step of distributed model in graph mode."""

def _per_replica_function(model):
    f = model._make_execution_function(mode)
    exit((f.inputs, f.outputs, f.updates_op, f.session_kwargs))

strategy = model._distribution_strategy
with strategy.scope():
    # Create train ops on each of the devices when we call
    # `_per_replica_fit_function`.
    (grouped_inputs, grouped_outputs, grouped_updates,
     grouped_session_args) = strategy.extended.call_for_each_replica(
         _per_replica_function, args=(get_distributed_model(model, mode),))

    # Initialize the variables in the replicated model. This is necessary for
    # multi-worker training because on some workers, initialization is not
    # needed. This method does initialization or waiting for initialization
    # according to the context object of distribute coordinator.
    init_restore_or_wait_for_variables()

    # Unwrap all the per device values returned from `call_for_each_replica`.
    # Unwrapping per device values gives you a list of values that can be
    # used to construct a new train function that is composed of update ops on
    # all the devices over which the model is distributed.
    (all_inputs, all_outputs, all_updates, all_session_args) = unwrap_values(
        strategy,
        grouped_inputs,
        grouped_outputs,
        grouped_updates,
        grouped_session_args,
        with_loss_tensor=(mode != ModeKeys.PREDICT))

    exit(backend.function(
        all_inputs,
        all_outputs,
        updates=all_updates,
        name='distributed_{}_function'.format(mode),
        **all_session_args))
