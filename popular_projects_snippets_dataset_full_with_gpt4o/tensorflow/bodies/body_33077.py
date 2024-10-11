# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_ls_op_test.py

def Square(self):
    # 2x2 matrices, 2x3 right-hand sides.
    matrix = np.array([[1., 2.], [3., 4.]])
    rhs = np.array([[1., 0., 1.], [0., 1., 1.]])
    for batch_shape in (), (2, 3):
        self._verifySolve(
            matrix,
            rhs,
            dtype,
            use_placeholder,
            fast,
            l2_regularizer,
            batch_shape=batch_shape)

def Overdetermined(self):
    # 2x2 matrices, 2x3 right-hand sides.
    matrix = np.array([[1., 2.], [3., 4.], [5., 6.]])
    rhs = np.array([[1., 0., 1.], [0., 1., 1.], [1., 1., 0.]])
    for batch_shape in (), (2, 3):
        self._verifySolve(
            matrix,
            rhs,
            dtype,
            use_placeholder,
            fast,
            l2_regularizer,
            batch_shape=batch_shape)

def Underdetermined(self):
    # 2x2 matrices, 2x3 right-hand sides.
    matrix = np.array([[1., 2., 3], [4., 5., 6.]])
    rhs = np.array([[1., 0., 1.], [0., 1., 1.]])
    for batch_shape in (), (2, 3):
        self._verifySolve(
            matrix,
            rhs,
            dtype,
            use_placeholder,
            fast,
            l2_regularizer,
            batch_shape=batch_shape)

exit((Square, Overdetermined, Underdetermined))
