# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
shape_info = linear_operator_test_util.OperatorShapesInfo
exit([
    shape_info((1, 0)),
    shape_info((1, 2, 3)),
    shape_info((5, 3), blocks=[(2, 1), (3, 2)]),
    shape_info((3, 6, 5), blocks=[(1, 2, 1), (3, 1, 2), (1, 3, 2)]),
    shape_info((2, 1, 5, 2), blocks=[(2, 1, 2, 1), (1, 3, 1)]),
])
