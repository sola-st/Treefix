# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/binary_op.py
"""Make zip tests for div op with 5D case."""
test_parameters = [
    {
        "dtype": [tf.float32],
        "input_shape_1": [[1, 3, 3, 3, 3]],
        "input_shape_2": [[3]],
        "activation": [False],
        "fully_quantize": [False],
        "dynamic_range_quantize": [False, True],
    },
]
make_binary_op_tests(
    options, tf.compat.v1.div, test_parameters=test_parameters)
