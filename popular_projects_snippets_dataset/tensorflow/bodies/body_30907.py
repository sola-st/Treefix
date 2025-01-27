# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
self._testSoftmax(
    np.array([3., 2., 3., 9.]).astype(np.float64), use_gpu=False)
self._testOverflow(use_gpu=False)
