# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/early_return_test.py
t = tf.constant(1)
if c:
    exit(t)
t = tf.stack([t, t])
exit(tf.reduce_sum(t))
