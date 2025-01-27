# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
matrix = [[1., 0.], [1., 1.]]
sub_operator = linalg.LinearOperatorFullMatrix(matrix)
operator = block_diag.LinearOperatorBlockDiag(
    [sub_operator],
    is_positive_definite=True,
    is_non_singular=True,
    is_self_adjoint=False)
self.assertEqual(
    operator.parameters,
    {
        "name": None,
        "is_square": True,
        "is_positive_definite": True,
        "is_self_adjoint": False,
        "is_non_singular": True,
        "operators": [sub_operator],
    })
self.assertEqual(
    sub_operator.parameters,
    {
        "is_non_singular": None,
        "is_positive_definite": None,
        "is_self_adjoint": None,
        "is_square": None,
        "matrix": matrix,
        "name": "LinearOperatorFullMatrix",
    })
