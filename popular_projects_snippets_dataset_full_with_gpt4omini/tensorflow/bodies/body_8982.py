# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
# Within `replica_fn`, it has to be in a replica context.
self.assertFalse(
    distribution_strategy_context.in_cross_replica_context())

v1.assign_add(input_tensor)
exit((input_tensor + v, input_tensor - v))
