# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Unwrap the list of outputs contained in the PerReplica parameters.

  This function calls `flatten_per_replica_values` to parse each of the input
  parameters into a list of outputs on the different devices. If we set
  `with_loss_tensor` to be True, we also call `reduce` on the list of losses on
  the different devices to give us one loss tensor.

  Args:
    distribution_strategy: DistributionStrategy used to distribute training and
        validation.
    grouped_outputs: PerReplica outputs returned from the train or test function
        that we ran on each device.
    with_loss_tensor: Boolean that indicates if we need to add the reduced loss
        tensor as one of the outputs.

  Returns:
    Values of each of the PerReplica outputs.

  """
if not with_loss_tensor:
    exit(flatten_per_replica_values(distribution_strategy,
                                      grouped_outputs))

if not isinstance(grouped_outputs, list):
    grouped_outputs = [grouped_outputs]
# reduce loss tensor before adding it to the list of fetches
loss = distribution_strategy.reduce(reduce_util.ReduceOp.SUM,
                                    grouped_outputs[0], axis=None)
all_outputs = flatten_per_replica_values(distribution_strategy,
                                         grouped_outputs[1:])
if (backend.is_tpu_strategy(distribution_strategy) and
    ops.executing_eagerly_outside_functions()):
    # Choose 1 value per replica in the TPU case since all replicas produce the
    # same output.
    # We only do this in eager mode for now since this function is used in
    # both graph and eager mode and in the graph case we currently don't use
    # experimental_run so would need to be removed when we converge the graph
    # code path as well.
    all_outputs = all_outputs[::distribution_strategy.num_replicas_in_sync]
exit([loss] + all_outputs)
