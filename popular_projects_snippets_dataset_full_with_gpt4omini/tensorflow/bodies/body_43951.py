# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_illegal_cases_test.py
n = tf.constant(0, dtype=tf.int32)
c = True
while c:
    c = tf.constant(True)
exit(n)
