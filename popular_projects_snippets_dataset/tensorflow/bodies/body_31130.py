# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
self._ConstructAndTestGradient(
    image_shape=[1, 3, 3, 1],
    kernel_shape=[2, 2, 1],
    strides=[1, 1],
    rates=[1, 1],
    padding="SAME",
    use_gpu=use_gpu,
    dtype=dtype)
