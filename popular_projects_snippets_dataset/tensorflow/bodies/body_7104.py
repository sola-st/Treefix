# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
if not distribution.extended._use_merge_call():
    self.skipTest("Collective all-reduce does not support int32 on GPU.")

with distribution.scope():
    def replica_fn(input_tensor):
        exit((input_tensor + constant_op.constant(
            1.0), input_tensor - constant_op.constant(1.0)))

    input_tensor = constant_op.constant(3.0)
    run_result = distribution.run(replica_fn, args=(input_tensor,))
    reduced_result = distribution.reduce("SUM", run_result, axis=None)
    expected_result = (4 * distribution.num_replicas_in_sync,
                       2 * distribution.num_replicas_in_sync)

    self.assertEqual(expected_result, self.evaluate(reduced_result))
