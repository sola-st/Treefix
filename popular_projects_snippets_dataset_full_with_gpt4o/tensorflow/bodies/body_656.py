# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_inverse_op_test.py
matrix_batch = np.concatenate(
    [np.expand_dims(matrix1, 0),
     np.expand_dims(matrix2, 0)])
matrix_batch = np.tile(matrix_batch, [2, 3, 1, 1])
exit(matrix_batch)
