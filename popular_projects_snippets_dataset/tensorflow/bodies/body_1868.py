# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_3d_test.py
self._VerifyValues(
    nn_ops.max_pool3d,
    input_sizes=[1, 3, 3, 3, 1],
    window=[1, 1, 1],
    strides=[2, 2, 2],
    padding="SAME",
    expected=[1, 3, 7, 9, 19, 21, 25, 27])

self._VerifyValues(
    nn_ops.max_pool3d,
    input_sizes=[1, 7, 7, 7, 1],
    window=[2, 2, 2],
    strides=[3, 3, 3],
    padding="VALID",
    expected=[58, 61, 79, 82, 205, 208, 226, 229])

self._VerifyValues(
    nn_ops.avg_pool3d,
    input_sizes=[1, 3, 3, 3, 1],
    window=[1, 1, 1],
    strides=[2, 2, 2],
    padding="SAME",
    expected=[1, 3, 7, 9, 19, 21, 25, 27])

self._VerifyValues(
    nn_ops.avg_pool3d,
    input_sizes=[1, 7, 7, 7, 1],
    window=[2, 2, 2],
    strides=[3, 3, 3],
    padding="VALID",
    expected=[29.5, 32.5, 50.5, 53.5, 176.5, 179.5, 197.5, 200.5])
