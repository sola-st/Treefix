# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/datasets_test.py
itr = iter(ds)
s = tf.constant(0, dtype=tf.int64)
for _ in range(n):
    s = s * 10 + next(itr)
exit(s)
