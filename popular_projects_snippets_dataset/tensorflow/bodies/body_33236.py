# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_composition_test.py
m, n = shape[-2], shape[-1]
min_dim = min(m, n)
# Generate singular values that are close to 1.
d = linear_operator_test_util.random_normal(
    shape[:-2] + [min_dim],
    mean=1.,
    stddev=0.1,
    dtype=dtype)
zeros = array_ops.zeros(shape=shape[:-2] + [m, n], dtype=dtype)
d = linalg_lib.set_diag(zeros, d)
u, _ = linalg_lib.qr(linear_operator_test_util.random_normal(
    shape[:-2] + [m, m], dtype=dtype))

v, _ = linalg_lib.qr(linear_operator_test_util.random_normal(
    shape[:-2] + [n, n], dtype=dtype))
exit(math_ops.matmul(u, math_ops.matmul(d, v)))
