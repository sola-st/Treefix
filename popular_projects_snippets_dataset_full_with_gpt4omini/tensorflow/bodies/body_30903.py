# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
self._testSoftmax(
    np.array([[1., 1., 1., 1.], [1., 2., 3., 4.]]).astype(np.float64))
self._testOverflow()
