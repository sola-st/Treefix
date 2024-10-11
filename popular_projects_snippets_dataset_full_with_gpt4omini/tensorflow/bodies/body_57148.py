# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reduce.py
"""Make a set of tests to do all."""
exit(make_reduce_tests(tf.reduce_all, boolean_tensor_only=True)(options))
