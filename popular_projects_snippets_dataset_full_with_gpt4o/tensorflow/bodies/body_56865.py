# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/elementwise.py
"""Make a set of tests to do 1/sqrt."""
exit(_make_elementwise_tests(tf.math.rsqrt, allow_fully_quantize=True,
                               min_value=.1, max_value=1)(options))
