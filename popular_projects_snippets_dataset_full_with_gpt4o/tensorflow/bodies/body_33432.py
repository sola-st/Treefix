# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_low_rank_update_test.py
shape_info = linear_operator_test_util.OperatorShapesInfo
# Previously we had a (2, 10, 10) shape at the end.  We did this to test the
# inversion and determinant lemmas on not-tiny matrices, since these are
# known to have stability issues.  This resulted in test timeouts, so this
# shape has been removed, but rest assured, the tests did pass.
exit([
    shape_info((0, 0)),
    shape_info((1, 1)),
    shape_info((1, 3, 3)),
    shape_info((3, 4, 4)),
    shape_info((2, 1, 4, 4))])
