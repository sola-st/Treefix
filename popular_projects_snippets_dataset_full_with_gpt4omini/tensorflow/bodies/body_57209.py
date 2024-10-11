# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/logic.py
"""Make a set of tests to do logical_xor, test logical_not as well."""
exit(_make_logical_tests(tf.math.logical_xor)(
    options, expected_tf_failures=1))
