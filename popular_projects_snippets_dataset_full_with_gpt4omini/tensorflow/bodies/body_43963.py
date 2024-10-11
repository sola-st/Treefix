# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_illegal_cases_test.py
s = [tf.constant(0)]
for _ in l:
    s = s + [tf.constant(0)]
exit(s)
