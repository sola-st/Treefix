# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_zeros_test.py
shapes_info = linear_operator_test_util.OperatorShapesInfo
exit([
    shapes_info((1, 1)),
    shapes_info((1, 3, 3)),
    shapes_info((3, 4, 4)),
    shapes_info((2, 1, 4, 4))])
