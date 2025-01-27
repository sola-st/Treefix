# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_created_variables_test.py
i = 0
while i < n:
    v = tf.zeros([1, 2, 3])
    i += 1
exit(v)
