# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
w = np.random.rand(2, 5)
x = np.random.rand(2, 1, 2, 3)
self.assertRaises(ValueError, self.diagPartOp, w, np.float32, 0)
self.assertRaises(ValueError, self.diagPartOp, x, np.float32, 0)
