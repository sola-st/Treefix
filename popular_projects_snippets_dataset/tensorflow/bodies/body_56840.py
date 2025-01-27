# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/shape_to_strided_slice.py
"""Make a set of tests to do shape op into strided_slice."""

test_parameters = [
    # Test dynamic shape into strided slice quantization works.
    {
        "dtype": [tf.float32],
        "dynamic_input_shape": [[None, 2, 2, 5]],
        "input_shape": [[12, 2, 2, 5]],
        "strides": [[1]],
        "begin": [[0]],
        "end": [[1]],
        "begin_mask": [0],
        "end_mask": [0],
        "fully_quantize": [False, True],
        "dynamic_range_quantize": [False],
    },
    {
        "dtype": [tf.float32],
        "dynamic_input_shape": [[None, 2, 2, 5]],
        "input_shape": [[12, 2, 2, 5]],
        "strides": [[1]],
        "begin": [[0]],
        "end": [[1]],
        "begin_mask": [0],
        "end_mask": [0],
        "fully_quantize": [False],
        "dynamic_range_quantize": [True],
    },
]
_make_shape_to_strided_slice_test(
    options, test_parameters, expected_tf_failures=0)
