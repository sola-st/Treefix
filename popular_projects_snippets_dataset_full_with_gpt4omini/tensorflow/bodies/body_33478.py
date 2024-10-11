# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/self_adjoint_eig_op_test.py
a = np.random.uniform(
    low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)
if dtype_.is_complex:
    a += 1j * np.random.uniform(
        low=-1.0, high=1.0, size=n * n).reshape([n, n]).astype(np_dtype)
a += np.conj(a.T)
a = np.tile(a, batch_shape + (1, 1))
exit(a)
