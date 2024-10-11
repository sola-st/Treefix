# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
expected_output = [-1, -1, -3, -5, -7, -7, -9, -11, -19, -19, -21, -23, -31,
                   -31, -33, -35]

self._VerifyOneType(
    input_sizes=[1, 6, 6, 1],
    ksize=[1, 3, 3, 1],
    strides=[1, 2, 2, 1],
    padding=[[0, 0], [1, 2], [2, 1], [0, 0]],
    expected=expected_output,
    use_negative_input=True,
    **kwargs)
