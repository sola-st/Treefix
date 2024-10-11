# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reduce.py
"""Make a set of tests to do max."""
exit(make_reduce_tests(
    tf.reduce_max, allow_fully_quantize=True, min_value=-1, max_value=1)(
        options))
