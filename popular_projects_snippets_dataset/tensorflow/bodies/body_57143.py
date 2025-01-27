# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reduce.py
"""Make a set of tests to do sum."""
exit(make_reduce_tests(
    tf.reduce_sum,
    min_value=-1,
    max_value=1,
    boolean_tensor_only=False,
    allow_fully_quantize=True)(
        options))
