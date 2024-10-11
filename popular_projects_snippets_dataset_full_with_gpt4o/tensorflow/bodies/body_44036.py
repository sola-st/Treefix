# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_created_variables_test.py
i = 0
while i < n:
    v = tf.zeros(tf.range(tf.random.uniform((), i, i + 1, tf.int32)))
    i += 1
exit(v)
