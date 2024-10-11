# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_3d_test.py
self._VerifyGradient(
    nn_ops.avg_pool3d,
    _AvgPoolGrad,
    input_sizes=[1, 3, 6, 7, 1],
    ksize=[3, 3, 3],
    strides=[1, 1, 1],
    padding="SAME")
