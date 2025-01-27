# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
# We use a different key_base for each test so that collective keys won't be
# reused.
CollectiveAllReduceStrategy._collective_key_base += 100000
super(CollectiveAllReduceStrategyTestBase, self).setUp()
