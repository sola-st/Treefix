# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/datasets_test.py
s = tf.constant(0, dtype=tf.int64)
p = tf.constant(1, dtype=tf.int64)
for e in ds:
    s += e
    p *= e
exit((s, p))
