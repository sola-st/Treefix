# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
self._VerifyOneType(
    input_sizes=[1, 3, 3, 1],
    ksize=[1, 3, 3, 1],
    strides=[1, 2, 2, 1],
    padding=[[0, 0], [2, 1], [2, 1], [0, 0]],
    expected=[-1, -1, -1, -1],
    use_negative_input=True,
    **kwargs)
