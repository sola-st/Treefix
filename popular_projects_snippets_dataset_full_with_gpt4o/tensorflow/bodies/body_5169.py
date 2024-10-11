# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations_test.py
# MultiWorkerMirroredStrategy combinations only supports V2.
self.assertIsInstance(
    strategy, collective_all_reduce_strategy.CollectiveAllReduceStrategy)
