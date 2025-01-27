# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
self._ConstructAndTestGradient(
    nn_ops.avg_pool3d,
    input_sizes=[1, 3, 6, 2, 1],
    output_sizes=[1, 3, 6, 2, 1],
    window=(3, 3, 3),
    strides=(1, 1, 1),
    padding="SAME")
