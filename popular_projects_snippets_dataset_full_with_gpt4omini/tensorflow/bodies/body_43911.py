# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_distributed_test.py
strat, ds = _distributed_dataset()
exit((strat, iter(ds)))
