# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/datasets_test.py
# This case will raise, but not the expected StopIteration error.
itr = iter(ds)
while cond:
    next(itr)
