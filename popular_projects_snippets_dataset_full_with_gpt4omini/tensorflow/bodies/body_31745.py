# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
self._ConstructAndTestGradient(
    nn_ops.max_pool3d,
    input_sizes=[1, 3, 3, 3, 1],
    output_sizes=[1, 2, 2, 2, 1],
    window=(1, 1, 1),
    strides=(2, 2, 2),
    padding="VALID")
