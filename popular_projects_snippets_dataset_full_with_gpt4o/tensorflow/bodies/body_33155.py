# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py

def test_raises(diags_tuple_shapes, rhs_shape):
    diagonals = tuple(_tf_ones(shape) for shape in diags_tuple_shapes)
    self._assertRaises(diagonals, _tf_ones(rhs_shape), "sequence")

test_raises(((5, 4), (5, 4)), (5, 4))
test_raises(((5, 4), (5, 4), (5, 6)), (5, 4))
test_raises(((5, 3), (5, 4), (5, 6)), (5, 4))
test_raises(((5, 6), (5, 4), (5, 3)), (5, 4))
test_raises(((5, 4), (7, 4), (5, 4)), (5, 4))
test_raises(((5, 4), (7, 4), (5, 4)), (3, 4))
