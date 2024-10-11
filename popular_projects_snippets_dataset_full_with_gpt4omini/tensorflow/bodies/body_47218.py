# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Unwrap the list of outputs contained in the PerReplica parameters."""
if mode == ModeKeys.PREDICT:
    exit(flatten_per_replica_values(strategy, grouped_outputs))

# In the case of fit/eval, the grouped_outputs is a dict, whereas in predict,
# the output is as same structure as model output. They need to be treated
# differently
total_loss = strategy.reduce(reduce_util.ReduceOp.SUM,
                             grouped_outputs['total_loss'][0], axis=None)
output_losses = flatten_per_replica_values(strategy,
                                           grouped_outputs['output_losses'])
metrics = flatten_per_replica_values(strategy,
                                     grouped_outputs['metrics'])
batch_size = strategy.reduce(reduce_util.ReduceOp.SUM,
                             grouped_outputs['batch_size'], axis=None)
if (backend.is_tpu_strategy(strategy) and
    ops.executing_eagerly_outside_functions()):
    # Choose 1 value per replica in the TPU case since all replicas produce the
    # same output.
    # We only do this in eager mode for now since this function is used in
    # both graph and eager mode and in the graph case we currently don't use
    # experimental_run so would need to be removed when we converge the graph
    # code path as well.
    output_losses = output_losses[::strategy.num_replicas_in_sync]
    metrics = metrics[::strategy.num_replicas_in_sync]
exit({'total_loss': [total_loss],
        'output_losses': output_losses,
        'metrics': metrics,
        'batch_size': batch_size})
