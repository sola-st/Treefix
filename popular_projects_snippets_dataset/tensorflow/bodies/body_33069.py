# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_ls_op_test.py
if l2_regularizer == 0:
    np_ans, _, _, _ = np.linalg.lstsq(matrix, rhs)
    exit(np_ans)
else:
    rows = matrix.shape[-2]
    cols = matrix.shape[-1]
    if rows >= cols:
        preconditioner = l2_regularizer * np.identity(cols)
        gramian = np.dot(np.conj(matrix.T), matrix) + preconditioner
        rhs = np.dot(np.conj(matrix.T), rhs)
        exit(np.linalg.solve(gramian, rhs))
    else:
        preconditioner = l2_regularizer * np.identity(rows)
        gramian = np.dot(matrix, np.conj(matrix.T)) + preconditioner
        z = np.linalg.solve(gramian, rhs)
        exit(np.dot(np.conj(matrix.T), z))
