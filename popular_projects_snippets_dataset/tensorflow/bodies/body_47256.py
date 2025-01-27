# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Makes function to run one step of distributed model eager execution."""
def _per_replica_function(model):
    f = model._make_execution_function(mode)
    exit((f.inputs, f.outputs))

# NOTE(priyag): Try creating a new FuncGraph within DS scope instead of using
# the global one.
strategy = model._distribution_strategy
global_graph = backend.get_graph()

with global_graph.as_default(), strategy.scope():
    # First we gather the relevant portions of the model across all replicas.
    # `backend._scratch_graph(global_graph)` signals to Keras that it should not
    # lift to a separate graph when creating the per-replica functions.
    with backend._scratch_graph(global_graph):
        # Create train ops on each of the devices when we call
        # `_per_replica_fit_function`.
        grouped = strategy.extended.call_for_each_replica(
            _per_replica_function, args=(get_distributed_model(model, mode),))
        grouped_inputs, grouped_outputs = grouped

        # Unwrap all the per device values returned from `call_for_each_replica`.
        # Unwrapping per device values gives you a list of values that can be
        # used to construct a new train function that is composed of
        # inputs/outputs on all the devices over which the model is distributed.
        (all_inputs, all_outputs, _, _) = unwrap_values(
            strategy,
            grouped_inputs,
            grouped_outputs,
            with_loss_tensor=(mode != ModeKeys.PREDICT))

    # Finally, a joint Keras function is created; this one will be created in
    # a separate FuncGraph.
    exit(backend.function(
        all_inputs,
        all_outputs,
        name='eager_distributed_{}_function'.format(mode)))
