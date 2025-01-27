# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_ls_op_test.py

def LargeBatchSquare(self):
    np.random.seed(1)
    num_rhs = 1
    matrix_shape = (127, 127)
    matrix = np.random.uniform(
        low=-1.0, high=1.0,
        size=np.prod(matrix_shape)).reshape(matrix_shape).astype(np.float32)
    rhs = np.ones([matrix_shape[0], num_rhs]).astype(np.float32)
    self._verifySolve(
        matrix,
        rhs,
        dtype,
        use_placeholder,
        fast,
        l2_regularizer,
        batch_shape=(16, 8))

def LargeBatchOverdetermined(self):
    np.random.seed(1)
    num_rhs = 1
    matrix_shape = (127, 64)
    matrix = np.random.uniform(
        low=-1.0, high=1.0,
        size=np.prod(matrix_shape)).reshape(matrix_shape).astype(np.float32)
    rhs = np.ones([matrix_shape[0], num_rhs]).astype(np.float32)
    self._verifySolve(
        matrix,
        rhs,
        dtype,
        use_placeholder,
        fast,
        l2_regularizer,
        batch_shape=(16, 8))

def LargeBatchUnderdetermined(self):
    np.random.seed(1)
    num_rhs = 1
    matrix_shape = (64, 127)
    matrix = np.random.uniform(
        low=-1.0, high=1.0,
        size=np.prod(matrix_shape)).reshape(matrix_shape).astype(np.float32)
    rhs = np.ones([matrix_shape[0], num_rhs]).astype(np.float32)
    self._verifySolve(
        matrix,
        rhs,
        dtype,
        use_placeholder,
        fast,
        l2_regularizer,
        batch_shape=(16, 8))

exit((LargeBatchSquare, LargeBatchOverdetermined, LargeBatchUnderdetermined))
