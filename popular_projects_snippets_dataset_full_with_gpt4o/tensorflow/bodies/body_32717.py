# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
matrices1 = []
for i in range(1, 5):
    matrices1.append(linalg.LinearOperatorFullMatrix(
        linear_operator_test_util.random_normal(
            [i, i], dtype=dtypes.float32)))
operator1 = block_diag.LinearOperatorBlockDiag(matrices1)
operator2 = linalg.LinearOperatorFullMatrix(
    linear_operator_test_util.random_normal(
        [15, 3], dtype=dtypes.float32))

with self.assertRaisesRegex(ValueError, "Operators are incompatible"):
    operator1.solve(operator2)
