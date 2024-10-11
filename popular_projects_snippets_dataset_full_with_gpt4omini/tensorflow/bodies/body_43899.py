# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_distributed_test.py
for pr in iterable:
    tf.print(strat.reduce('SUM', pr, axis=0))
