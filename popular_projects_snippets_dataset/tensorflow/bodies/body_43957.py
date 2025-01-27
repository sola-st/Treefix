# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_illegal_cases_test.py
t = tf.constant([1])
for _ in l:
    t = tf.constant([1, 1])
exit(t)
