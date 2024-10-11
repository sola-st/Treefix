# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
with self.assertRaisesRegex(ValueError, "non-empty"):
    block_diag.LinearOperatorBlockDiag([])
