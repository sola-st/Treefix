# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_distributed_test.py
itr = iter(iterable)
a = strat.reduce('SUM', next(itr), axis=0)
b = strat.reduce('SUM', next(itr), axis=0)
exit(a * 10 + b)
