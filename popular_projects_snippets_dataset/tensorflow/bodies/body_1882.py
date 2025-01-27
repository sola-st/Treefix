# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_3d_test.py
self._VerifyGradient(
    nn_ops.avg_pool3d,
    _AvgPoolGrad,
    input_sizes=[1, 2, 2, 2, 1],
    ksize=[2, 2, 2],
    strides=[1, 1, 1],
    padding="SAME")
