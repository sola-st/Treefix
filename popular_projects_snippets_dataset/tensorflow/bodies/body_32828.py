# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/eig_op_test.py
perm = np.argsort(e.real + e.imag, -1)
exit(np.take(e, perm, -1))
