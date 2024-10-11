# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reduce.py
"""Make a set of tests to do prod."""
# set min max value to be -2, 2 to avoid overflow.
exit(make_reduce_tests(tf.reduce_prod, -2, 2)(options))
