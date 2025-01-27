# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('/job:worker'):
    # Multiple worker tasks, thus ambiguous device found error will be
    # raised.
    exit(i + constant_op.constant([2]))
