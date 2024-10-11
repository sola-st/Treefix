# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/strided_slice.py
"""Make a set of exhaustive tests for 1D strided_slice."""
test_parameters = [
    # 1-D Exhaustive
    {
        "dtype": [tf.float32],
        "index_type": [tf.int32],
        "input_shape": [[3]],
        "begin": [[-2], [-1], [0], [1], [2]],
        "end": [[-2], [-1], [0], [1], [2]],
        "strides": [[-2], [-1], [1], [2]],
        "begin_mask": [0, 1],
        "end_mask": [0, 1],
        "shrink_axis_mask": [0],
        "constant_indices": [False],
    },
]
_make_strided_slice_tests(options, test_parameters)
