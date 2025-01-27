# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_toeplitz_test.py
shape_info = linear_operator_test_util.OperatorShapesInfo
# non-batch operators (n, n) and batch operators.
exit([
    shape_info((1, 1)),
    shape_info((1, 6, 6)),
    shape_info((3, 4, 4)),
    shape_info((2, 1, 3, 3))
])
