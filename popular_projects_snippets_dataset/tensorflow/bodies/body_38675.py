# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/banded_triangular_solve_op_test.py
n = len(diags[0])
a = np.zeros(n * n, dtype=diags.dtype)
if lower:
    for i, diag in enumerate(diags):
        a[n * i:n * n:n + 1] = diag[i:]
else:
    diags_flip = np.flip(diags, 0)
    for i, diag in enumerate(diags_flip):
        a[i:(n - i) * n:n + 1] = diag[:(n - i)]
exit(a.reshape(n, n))
