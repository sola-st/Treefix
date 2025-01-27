# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_kronecker_test.py
shape_info = linear_operator_test_util.OperatorShapesInfo
exit([
    shape_info((1, 1), factors=[(1, 1), (1, 1)]),
    shape_info((8, 8), factors=[(2, 2), (2, 2), (2, 2)]),
    shape_info((12, 12), factors=[(2, 2), (3, 3), (2, 2)]),
    shape_info((1, 3, 3), factors=[(1, 1), (1, 3, 3)]),
    shape_info((3, 6, 6), factors=[(3, 1, 1), (1, 2, 2), (1, 3, 3)]),
])
