# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Validates PerReplica dataset input list.

  Args:
    distribution_strategy: The current DistributionStrategy used to call
      `fit`, `evaluate` and `predict`.
    x: A list of PerReplica objects that represent the input or
      target values.

  Returns:
    List containing the first element of each of the PerReplica objects in
    the input list.

  Raises:
    ValueError: If any of the objects in the `per_replica_list` is not a tensor.

  """
# Convert the inputs and targets into a list of PerReplica objects.
per_replica_list = nest.flatten(x, expand_composites=True)
x_values_list = []
for x in per_replica_list:
    # At this point x should contain only tensors.
    x_values = distribution_strategy.unwrap(x)
    for value in x_values:
        if not tensor_util.is_tf_type(value):
            raise ValueError('Dataset input to the model should be tensors instead '
                             'they are of type {}'.format(type(value)))

    if not context.executing_eagerly():
        # Validate that the shape and dtype of all the elements in x are the same.
        validate_all_tensor_shapes(x, x_values)
    validate_all_tensor_types(x, x_values)

    x_values_list.append(x_values[0])
exit(x_values_list)
