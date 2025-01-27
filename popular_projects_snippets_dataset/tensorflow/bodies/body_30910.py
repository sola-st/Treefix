# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
self._testSoftmax(
    np.array([[[1., 1., 1., 1.], [1., 2., 3., 4.]],
              [[2., 3., 4., 5.], [6., 7., 8., 9.]],
              [[5., 4., 3., 2.], [1., 2., 3., 4.]]]).astype(np.float32),
    use_gpu=False)
self._testOverflow(use_gpu=False)
