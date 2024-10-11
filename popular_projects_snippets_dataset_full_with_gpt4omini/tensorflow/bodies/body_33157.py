# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py

def test_raises(diags_shape, rhs_shape):
    self._assertRaises(_tf_ones(diags_shape), _tf_ones(rhs_shape), "matrix")

test_raises((5, 4, 7), (5, 4))
test_raises((5, 4, 4), (3, 4))
test_raises((5, 4, 4), (5, 3))
