# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py

def test_raises(diags_shape, rhs_shape):
    self._assertRaises(_tf_ones(diags_shape), _tf_ones(rhs_shape), "matrix")

test_raises((5, 4, 7), (5, 4))
test_raises((5, 4, 4), (3, 4))
test_raises((5, 4, 4), (5, 3))
