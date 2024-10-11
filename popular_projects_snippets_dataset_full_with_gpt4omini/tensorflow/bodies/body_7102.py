# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
if not distribution.extended._use_merge_call():
    self.skipTest("Collective all-reduce does not support int32 on GPU.")

with distribution.scope():
    result = distribution.extended.call_for_each_replica(_replica_id)
    reduced = distribution.reduce(reduce_util.ReduceOp.SUM, result, axis=None)
    expected = sum(range(distribution.num_replicas_in_sync))
    self.assertEqual(expected, self.evaluate(reduced))
