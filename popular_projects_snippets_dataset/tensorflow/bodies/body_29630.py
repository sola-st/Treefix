# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.assertRaisesRegex(ValueError, "must be at least rank 1"):
    array_ops.matrix_diag(0)
