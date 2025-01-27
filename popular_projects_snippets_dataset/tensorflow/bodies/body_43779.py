# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/datasets_test.py
s = tf.constant(0, dtype=tf.int64)
for e in iter(ds):
    s = s * 10 + e
exit(s)
