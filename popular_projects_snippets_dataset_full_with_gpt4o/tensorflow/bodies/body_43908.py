# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_distributed_test.py
# This case will raise, but not the expected StopIteration error.
itr = iter(iterable)
while cond:
    strat.reduce('SUM', next(itr), axis=0)
