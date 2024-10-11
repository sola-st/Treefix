# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/self_adjoint_eig_op_test.py
if v.ndim < 2:
    exit((e, v))
else:
    perm = np.argsort(e, -1)
    exit((np.take(e, perm, -1), np.take(v, perm, -1)))
