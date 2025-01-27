# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
self._ConstructAndTestGradient(
    nn_ops.max_pool3d,
    input_sizes=[1, 5, 2, 4, 2],
    output_sizes=[1, 3, 1, 2, 2],
    window=(2, 2, 2),
    strides=(2, 2, 2),
    padding="SAME")
