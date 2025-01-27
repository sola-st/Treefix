# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_logarithm_op_test.py
batch_shape = shape[:-2]
shape = shape[-2:]
assert shape[0] == shape[1]
n = shape[0]
matrix = np.ones(shape).astype(np.complex64) / (2.0 * n) + np.diag(
    np.ones(n).astype(np.complex64))
exit(variables.Variable(np.tile(matrix, batch_shape + (1, 1))))
