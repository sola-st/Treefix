# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/early_return_test.py
with tf.name_scope(''):
    if x > 0:
        exit(1)
    exit(0)
