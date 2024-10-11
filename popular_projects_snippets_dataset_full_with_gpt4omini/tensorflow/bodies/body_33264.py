# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_toeplitz_test.py
shape = list(build_info.shape)
row = np.random.uniform(low=1., high=5., size=shape[:-1])
col = np.random.uniform(low=1., high=5., size=shape[:-1])

# Make sure first entry is the same
row[..., 0] = col[..., 0]

if ensure_self_adjoint_and_pd:
    # Note that a Toeplitz matrix generated from a linearly decreasing
    # non-negative sequence is positive definite. See
    # https://www.math.cinvestav.mx/~grudsky/Papers/118_29062012_Albrecht.pdf
    # for details.
    row = np.linspace(start=10., stop=1., num=shape[-1])

    # The entries for the first row and column should be the same to guarantee
    # symmetric.
    row = col

lin_op_row = math_ops.cast(row, dtype=dtype)
lin_op_col = math_ops.cast(col, dtype=dtype)

if use_placeholder:
    lin_op_row = array_ops.placeholder_with_default(
        lin_op_row, shape=None)
    lin_op_col = array_ops.placeholder_with_default(
        lin_op_col, shape=None)

operator = linear_operator_toeplitz.LinearOperatorToeplitz(
    row=lin_op_row,
    col=lin_op_col,
    is_self_adjoint=True if ensure_self_adjoint_and_pd else None,
    is_positive_definite=True if ensure_self_adjoint_and_pd else None)

flattened_row = np.reshape(row, (-1, shape[-1]))
flattened_col = np.reshape(col, (-1, shape[-1]))
flattened_toeplitz = np.zeros(
    [flattened_row.shape[0], shape[-1], shape[-1]])
for i in range(flattened_row.shape[0]):
    flattened_toeplitz[i] = scipy.linalg.toeplitz(
        flattened_col[i],
        flattened_row[i])
matrix = np.reshape(flattened_toeplitz, shape)
matrix = math_ops.cast(matrix, dtype=dtype)

exit((operator, matrix))
