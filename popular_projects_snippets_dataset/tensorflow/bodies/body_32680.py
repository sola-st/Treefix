# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
huge = 0.33 * np.finfo(dtype).max
tiny = 3 * np.finfo(dtype).tiny
for (a, b) in [(tiny, tiny), (huge, np.sqrt(huge))]:
    alpha = np.array([-a, -np.sqrt(a), np.sqrt(a), a]).astype(dtype)

    beta = b * np.ones([3], dtype=dtype)
    if np.issubdtype(alpha.dtype, np.complexfloating):
        beta += 1j * beta
