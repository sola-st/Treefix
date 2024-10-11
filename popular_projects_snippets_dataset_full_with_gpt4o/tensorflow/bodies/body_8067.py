# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
# It's not uncommon for people to special case MultiWorkerMirroredStrategy,
# so we need to make sure isinstance check works for combinations between
# the experimental and non-experimental endpoints.
strategy = CollectiveAllReduceStrategy()
experimental_strategy = _CollectiveAllReduceStrategyExperimental()
self.assertIsInstance(strategy, CollectiveAllReduceStrategy)
self.assertIsInstance(strategy, _CollectiveAllReduceStrategyExperimental)
self.assertIsInstance(experimental_strategy, CollectiveAllReduceStrategy)
self.assertIsInstance(experimental_strategy,
                      _CollectiveAllReduceStrategyExperimental)
