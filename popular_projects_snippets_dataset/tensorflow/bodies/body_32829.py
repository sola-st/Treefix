# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/eig_op_test.py
if v.ndim < 2:
    exit((e, v))
perm = np.argsort(e.real + e.imag, -1)
exit((np.take(e, perm, -1), np.take(v, perm, -1)))
