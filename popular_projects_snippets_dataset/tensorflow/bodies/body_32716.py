# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
matrices1 = []
matrices2 = []
for i in range(1, 5):
    matrices1.append(linalg.LinearOperatorFullMatrix(
        linear_operator_test_util.random_tril_matrix(
            [i, i],
            dtype=dtypes.float32,
            force_well_conditioned=True)))

    matrices2.append(linalg.LinearOperatorFullMatrix(
        linear_operator_test_util.random_normal(
            [i, 3], dtype=dtypes.float32)))

operator1 = block_diag.LinearOperatorBlockDiag(matrices1)
operator2 = block_diag.LinearOperatorBlockDiag(matrices2, is_square=False)

expected_matrix = linalg.solve(
    operator1.to_dense(), operator2.to_dense())
actual_operator = operator1.solve(operator2)

self.assertIsInstance(
    actual_operator, block_diag.LinearOperatorBlockDiag)
actual_, expected_ = self.evaluate([
    actual_operator.to_dense(), expected_matrix])
self.assertAllClose(actual_, expected_)
