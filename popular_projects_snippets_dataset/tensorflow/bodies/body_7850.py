# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
# CollectiveAllReduceStrategy and TPUStrategy must have a cluster resolver.
# `None` otherwise.
resolver = strategy.cluster_resolver
if (not isinstance(strategy, CollectiveAllReduceStrategy) and
    not strategy_test_lib.is_tpu_strategy(strategy)):
    self.assertIsNone(resolver)
    exit()

with strategy.scope():
    self.assertIs(strategy.cluster_resolver, resolver)

self.assertTrue(hasattr(resolver, 'cluster_spec'))
self.assertTrue(hasattr(resolver, 'master'))
self.assertTrue(hasattr(resolver, 'num_accelerators'))
self.assertTrue(hasattr(resolver, 'task_id'))
self.assertTrue(hasattr(resolver, 'task_type'))
if isinstance(strategy, CollectiveAllReduceStrategy):
    self.assertEqual(resolver.task_id, 0)
    self.assertAllInSet(resolver.task_type, ['chief', 'worker'])
