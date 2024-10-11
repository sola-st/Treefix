# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
matrices = constant_op.constant(1.0, shape=[0, 2, 2])
s, u, v = self.evaluate(linalg_ops.svd(matrices))
self.assertAllEqual(s, np.zeros([0, 2]))
self.assertAllEqual(u, np.zeros([0, 2, 2]))
self.assertAllEqual(v, np.zeros([0, 2, 2]))
