# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_lower_triangular_test.py
shape_info = linear_operator_test_util.OperatorShapesInfo
exit([
    shape_info((0, 0)),
    shape_info((1, 1)),
    shape_info((1, 3, 3)),
    shape_info((5, 5), blocks=[[(2, 2)], [(3, 2), (3, 3)]]),
    shape_info((3, 7, 7),
               blocks=[[(1, 2, 2)], [(1, 3, 2), (3, 3, 3)],
                       [(1, 2, 2), (1, 2, 3), (1, 2, 2)]]),
    shape_info((2, 4, 6, 6),
               blocks=[[(2, 1, 2, 2)], [(1, 4, 2), (4, 4, 4)]]),
])
