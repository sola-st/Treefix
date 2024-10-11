# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_3d_test.py
self._VerifyGradient(
    nn_ops.avg_pool3d,
    _AvgPoolGrad,
    input_sizes=[2, 2, 2, 2, 3],
    ksize=[2, 2, 2],
    strides=[2, 2, 2],
    padding="VALID")
