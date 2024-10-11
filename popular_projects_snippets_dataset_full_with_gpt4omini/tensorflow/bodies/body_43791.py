# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/datasets_test.py
# This is the only instance when the use of TF iterators does not work as
# intended. In graph mode, the `except` below will never catch, and the
# tf.function will raise the error instead.
# TODO(b/132311724): The error should be friendlier here.
# Note: b/132298783 covers actually supporting this pattern.
itr = iter(ds)
try:
    while cond:
        next(itr)
except StopIteration:
    pass
