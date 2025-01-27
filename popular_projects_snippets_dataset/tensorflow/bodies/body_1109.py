# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
diagonals = tuple(_tf_ones(shape) for shape in diags_tuple_shapes)
self._assertRaises(diagonals, _tf_ones(rhs_shape), "sequence")
