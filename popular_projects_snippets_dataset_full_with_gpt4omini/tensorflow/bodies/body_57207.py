# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/logic.py
"""Make a set of tests to do logical_or."""
exit(_make_logical_tests(tf.logical_or)(options, expected_tf_failures=1))
