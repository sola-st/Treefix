# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
matrix = [[11., 0.], [1., 8.]]
operator_1 = linalg.LinearOperatorFullMatrix(matrix, name="left")
operator_2 = linalg.LinearOperatorFullMatrix(matrix, name="right")

operator = block_diag.LinearOperatorBlockDiag([operator_1, operator_2])

self.assertEqual("left_ds_right", operator.name)
