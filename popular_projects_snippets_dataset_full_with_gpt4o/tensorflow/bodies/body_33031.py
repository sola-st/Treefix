# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
# Turn the random matrix x into a Hermitian matrix by
# computing the quadratic form x * x^H.
a = test_util.matmul_without_tf32(
    x, math_ops.conj(array_ops.matrix_transpose(x))) / shape[0]
if batch:
    a = array_ops.tile(array_ops.expand_dims(a, 0), [2, 1, 1])
# Finally take the cholesky decomposition of the Hermitian matrix.
c = linalg_ops.cholesky(a)
if scalar_test:
    # Reduce to a single scalar output to speed up test.
    c = math_ops.reduce_mean(c)
exit(c)
