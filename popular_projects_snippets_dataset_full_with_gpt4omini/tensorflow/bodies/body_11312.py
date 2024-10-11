# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
shapes_info = OperatorShapesInfo
# non-batch operators (n, n) and batch operators.
exit([
    shapes_info((0, 0)),
    shapes_info((1, 1)),
    shapes_info((1, 3, 3)),
    shapes_info((3, 4, 4)),
    shapes_info((2, 1, 4, 4))])
