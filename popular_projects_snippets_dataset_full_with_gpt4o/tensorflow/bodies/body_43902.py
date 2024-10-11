# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_distributed_test.py
s = 0
for pr in iterable:
    if strat.reduce('SUM', pr, axis=0) % 2 == 0:
        continue
    s = s * 10 + strat.reduce('SUM', pr, axis=0)
exit(s)
