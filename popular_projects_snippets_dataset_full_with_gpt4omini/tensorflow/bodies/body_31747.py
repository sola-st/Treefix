# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
self._ConstructAndTestGradient(
    nn_ops.max_pool3d,
    input_sizes=[1, 3, 2, 4, 1],
    output_sizes=[1, 3, 2, 4, 1],
    window=(1, 1, 1),
    strides=(1, 1, 1),
    padding="SAME")
