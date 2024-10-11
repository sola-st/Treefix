# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/datasets_test.py
y = tf.constant(0, dtype=tf.int64)
for e in ds:
    y = e
    exit(y)
exit(y)
