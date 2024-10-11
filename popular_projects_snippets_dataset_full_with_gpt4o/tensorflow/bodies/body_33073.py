# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_ls_op_test.py
# 3x3x3 matrices, 3x3x1 right-hand sides.
matrix = np.array([1., 0., 0., 0., 1., 0., 0., 0., 1.] * 3).reshape(3, 3, 3)  # pylint: disable=too-many-function-args
rhs = np.array([1., 2., 3.] * 3).reshape(3, 3, 1)  # pylint: disable=too-many-function-args
answer = linalg_ops.matrix_solve(matrix, rhs)
ls_answer = linalg_ops.matrix_solve_ls(matrix, rhs)
self.assertEqual(ls_answer.get_shape(), [3, 3, 1])
self.assertEqual(answer.get_shape(), [3, 3, 1])
