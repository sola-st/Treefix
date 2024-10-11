# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Validate all the components of a DistributedValue Dataset input.

  Args:
    distribution_strategy: The current DistributionStrategy used to call
        `fit`/`evaluate`.
    x: Input Dataset DistributedValue object. For example, when we use
        `MirroredStrategy` this is a PerReplica object with a tensor for each
        device set in the dict. x can also be a tuple or dict. The keys of the
        dict should match the names of the input layers of the model.
    y: Target Dataset DistributedValue object. For example, when we use
        `MirroredStrategy` this is a PerReplica object with a tensor for each
        device set in the dict. y can also be a tuple or dict. The keys of the
        dict should match the names of the output layers of the model.
    sample_weights: Sample weights Dataset DistributedValue object. For example,
        when we use `MirroredStrategy` this is a PerReplica object with a tensor
        for each device set in the dict.

  Returns:
    The unwrapped values list of the x and y DistributedValues inputs.

  Raises:
    ValueError: If x and y do not have support for being evaluated as tensors.
        or if x and y contain elements that are not tensors or if x and y
        contain elements that have a shape or dtype mismatch.
  """
# If the input and target used to call the model are not dataset tensors,
# we need to raise an error. When using a DistributionStrategy, the input
# and targets to a model should be from a `tf.data.Dataset`.

# If each element of x and y are not tensors, we cannot standardize and
# validate the input and targets.
x_values_list = validate_per_replica_inputs(distribution_strategy, x)

if y is not None:
    y_values_list = validate_per_replica_inputs(distribution_strategy, y)
else:
    y_values_list = None

if sample_weights is not None:
    sample_weights_list = validate_per_replica_inputs(distribution_strategy,
                                                      sample_weights)
else:
    sample_weights_list = None

# Return the unwrapped values to avoid calling `unwrap` a second time.
exit((x_values_list, y_values_list, sample_weights_list))
