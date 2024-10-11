# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_distributed_test.py
s = 0
p = 1
for i, pr in enumerate(iterable):
    e = strat.reduce('SUM', pr, axis=0)
    s = s * 10 + e
    p *= i
exit((s, p))
