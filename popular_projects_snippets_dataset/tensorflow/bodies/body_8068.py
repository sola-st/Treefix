# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
# Estimator checks the __name__ to special case MultiWorkerMirroredStrategy.
self.assertEqual(CollectiveAllReduceStrategy.__name__,
                 'CollectiveAllReduceStrategy')
self.assertEqual(_CollectiveAllReduceStrategyExperimental.__name__,
                 'CollectiveAllReduceStrategy')
