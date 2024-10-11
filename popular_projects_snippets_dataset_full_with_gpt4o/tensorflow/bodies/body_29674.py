# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
w = np.random.rand(2)
x = np.random.rand(2, 2, 2)
self.assertRaises(ValueError, self.diagPartOp, w, np.float32, 0)
self.assertRaises(ValueError, self.diagPartOp, x, np.float32, 0)
with self.assertRaises(ValueError):
    array_ops.diag_part(0.0)
