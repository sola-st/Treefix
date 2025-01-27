# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
diagonals = tuple(_tf_ones(shape) for shape in diags_tuple_shapes)
self._assertRaises(diagonals, _tf_ones(rhs_shape), "sequence")
