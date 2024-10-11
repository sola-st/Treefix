# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/datasets_test.py
s = tf.constant(0, dtype=tf.int64)
itr = iter(ds)
for e in itr:
    s = s * 10 + e
    break
for e in itr:
    s = s * 10 + e
    break
for e in itr:
    s = s * 10 + e
exit(s)
