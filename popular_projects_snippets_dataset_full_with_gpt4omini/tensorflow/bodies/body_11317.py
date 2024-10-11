# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
shapes_info = OperatorShapesInfo
# non-batch operators (n, n) and batch operators.
exit([
    shapes_info((2, 1)),
    shapes_info((1, 2)),
    shapes_info((1, 3, 2)),
    shapes_info((3, 3, 4)),
    shapes_info((2, 1, 2, 4))])
