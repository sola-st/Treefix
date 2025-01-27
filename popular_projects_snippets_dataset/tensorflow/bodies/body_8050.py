# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
strategy, _ = self._get_test_object(
    None, None, required_gpus, use_devices_arg=use_devices_arg)
with strategy.scope():
    result = strategy.extended.call_for_each_replica(_replica_id_f32)
    reduced = strategy.reduce(reduce_util.ReduceOp.SUM, result, axis=None)
    expected = sum(range(strategy.num_replicas_in_sync))
    self.assertEqual(expected, self.evaluate(reduced))
