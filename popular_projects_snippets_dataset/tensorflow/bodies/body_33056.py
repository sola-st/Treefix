# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_logarithm_op_test.py
matrix_batch = np.concatenate(
    [np.expand_dims(matrix1, 0),
     np.expand_dims(matrix2, 0)])
matrix_batch = np.tile(matrix_batch, [2, 3, 1, 1])
exit(matrix_batch)
