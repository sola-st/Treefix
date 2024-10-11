# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
if not test.is_gpu_available():
    exit()
self._testSeparableConv2D("NCHW")
