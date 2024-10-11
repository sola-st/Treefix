# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_illegal_cases_test.py
s = {'a': tf.constant(0)}
while tf.constant(True):
    s = tf.constant(7.0)
exit(s)
