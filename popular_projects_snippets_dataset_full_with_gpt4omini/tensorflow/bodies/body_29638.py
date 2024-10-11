# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.assertRaisesRegex(ValueError, "must be at least rank 2"):
    array_ops.matrix_set_diag(0, [0])
with self.assertRaisesRegex(ValueError, "must be at least rank 1"):
    array_ops.matrix_set_diag([[0]], 0)
