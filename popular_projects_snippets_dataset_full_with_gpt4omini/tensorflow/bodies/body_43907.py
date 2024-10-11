# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_distributed_test.py
itr = iter(iterable)
s = 0
for _ in l:
    s = s * 10 + strat.reduce('SUM', next(itr), axis=0)
exit(s)
