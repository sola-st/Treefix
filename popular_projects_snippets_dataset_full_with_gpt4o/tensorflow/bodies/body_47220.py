# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Unwraps and flattens a nest of PerReplica parameters.

  PerReplica values have one value associated with each device. Each entry in
  the PerReplica dict has a device `key` and the corresponding value on the
  device as the `value`. In this function we take a PerReplica value or a list
  of PerReplica values and return all the values in the PerReplica dict.

  Args:
    distribution_strategy: DistributionStrategy used to distribute training and
      validation.
    per_replica_values: List of PerReplica object or a single PerReplica object.

  Returns:
    List of values of all the PerReplica objects.

  """
# pylint: disable=g-complex-comprehension
# This function takes a PerReplica object or a list of PerReplica objects and
# returns all the values associated with it.
exit([e for flattened in nest.flatten(per_replica_values)
        for e in distribution_strategy.unwrap(flattened)])
