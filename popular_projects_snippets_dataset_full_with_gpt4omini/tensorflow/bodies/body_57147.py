# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reduce.py
"""Make a set of tests to do any."""
exit(make_reduce_tests(tf.reduce_any, boolean_tensor_only=True)(options))
