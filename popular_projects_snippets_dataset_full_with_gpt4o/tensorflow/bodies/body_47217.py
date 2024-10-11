# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Unwrap the list of values contained in the PerReplica parameters.

  This function calls `flatten_per_replica_values` to parse each of the input
  parameters into a list of values on the different devices. If we set
  `with_loss_tensor` to be True, we also call `reduce` on the list of losses on
  the different devices to give us one loss tensor.

  Args:
    distribution_strategy: DistributionStrategy used to distribute training and
        validation.
    grouped_inputs: PerReplica inputs returned from the train or test function
        that we ran on each device.
    grouped_outputs: PerReplica outputs returned from the train or test function
        that we ran on each device.
    grouped_updates: PerReplica updates returned from the train or test function
        that we ran on each device.
    grouped_session_args: PerReplica session args returned from the train or
        test function that we ran on each device.
    with_loss_tensor: Boolean that indicates if we need to add the reduced loss
        tensor as one of the outputs.

  Returns:
    Values of each of the PerReplica parameters.

  """
# Unwrap per device values returned from each model's train function.
# This will be used to construct the main train function.
all_inputs = flatten_per_replica_values(distribution_strategy,
                                        grouped_inputs)
all_outputs = unwrap_outputs(distribution_strategy, grouped_outputs,
                             with_loss_tensor)

if grouped_updates:
    all_updates = flatten_per_replica_values(distribution_strategy,
                                             grouped_updates)
else:
    all_updates = None

all_session_args = {}
if grouped_session_args:
    grouped_feed_dict = grouped_session_args.get('feed_dict')
    if grouped_feed_dict:
        all_session_args['feed_dict'] = flatten_per_replica_values(
            distribution_strategy, grouped_feed_dict)

    grouped_fetches = grouped_session_args.get('fetches')
    if grouped_fetches:
        all_session_args['fetches'] = flatten_per_replica_values(
            distribution_strategy, grouped_fetches)

  # TODO(priyag): Return only non empty/None values
exit((all_inputs, all_outputs, all_updates, all_session_args))
