# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
self._testSoftmax(features, dtype=dtype, use_gpu=True)
self._testSoftmax(features, dtype=dtype, log=True, use_gpu=True)
self._testOverflow(use_gpu=True)
