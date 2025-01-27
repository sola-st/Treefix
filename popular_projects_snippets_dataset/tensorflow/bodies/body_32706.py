# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
shape_info = linear_operator_test_util.OperatorShapesInfo
exit([
    shape_info((0, 0)),
    shape_info((1, 1)),
    shape_info((1, 3, 3)),
    shape_info((5, 5), blocks=[(2, 2), (3, 3)]),
    shape_info((3, 7, 7), blocks=[(1, 2, 2), (3, 2, 2), (1, 3, 3)]),
    shape_info((2, 1, 5, 5), blocks=[(2, 1, 2, 2), (1, 3, 3)]),
])
