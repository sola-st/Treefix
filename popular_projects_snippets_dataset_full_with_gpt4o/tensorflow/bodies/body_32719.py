# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
matrices = []
for _ in range(3):
    matrices.append(variables_module.Variable(
        linear_operator_test_util.random_positive_definite_matrix(
            [3, 3], dtype=dtypes.float32, force_well_conditioned=True)))

operator = block_diag.LinearOperatorBlockDiag(
    [linalg.LinearOperatorFullMatrix(
        matrix, is_self_adjoint=True,
        is_positive_definite=True) for matrix in matrices],
    is_self_adjoint=True,
    is_positive_definite=True,
)
with self.cached_session() as sess:
    sess.run([x.initializer for x in operator.variables])
    self.check_convert_variables_to_tensors(operator)
