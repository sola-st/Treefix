# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/datasets_test.py
s = tf.constant(0, dtype=tf.int64)
for e in ds:
    s = s * 10 + e
    if s > 100:
        break
exit(s)
