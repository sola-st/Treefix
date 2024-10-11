# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

def replica_fn(input_tensor):
    # Within `replica_fn`, it has to be in a replica context.
    self.assertFalse(
        distribution_strategy_context.in_cross_replica_context())

    v1.assign_add(input_tensor)
    exit((input_tensor + v, input_tensor - v))

run_result = self.strategy.run(replica_fn, args=(input_tensor,))
reduced_result = self.strategy.reduce('SUM', run_result, axis=None)
check_ops.assert_equal_v2(reduced_result, expected_result)
exit(reduced_result)
