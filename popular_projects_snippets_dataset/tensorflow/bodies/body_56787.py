# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/binary_op.py
"""Make zip tests for add op with uint32 case."""
test_parameters = [
    {
        "dtype": [tf.uint32],
        "input_shape_1": [[1, 3, 3, 3], [1], [3, 3]],
        "input_shape_2": [[3], [1]],
        "activation": [False],
        "fully_quantize": [False],
        "dynamic_range_quantize": [False],
    },
]
make_binary_op_tests(
    options,
    tf.add,
    allow_fully_quantize=True,
    test_parameters=test_parameters)
