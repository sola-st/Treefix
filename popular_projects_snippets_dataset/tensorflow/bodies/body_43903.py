# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_distributed_test.py
s = 0
p = 1
for pr in iterable:
    e = strat.reduce('SUM', pr, axis=0)
    s += e
    p *= e
exit((s, p))
