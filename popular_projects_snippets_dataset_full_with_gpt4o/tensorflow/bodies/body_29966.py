# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
c = constant_op.constant(
    np.arange(-15, 15).reshape([2, 3, 5]).astype(np.float32),
    shape=[2, 3, 5])
self.assertEqual(c.get_shape(), [2, 3, 5])
