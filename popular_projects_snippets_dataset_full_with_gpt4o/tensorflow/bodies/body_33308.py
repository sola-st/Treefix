# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
"""Slow but accurate Taylor series matrix exponential."""
y = np.zeros(x.shape, dtype=x.dtype)
xn = np.eye(x.shape[0], dtype=x.dtype)
for n in range(40):
    if n > 0:
        xn /= float(n)
    y += xn
    xn = np.dot(xn, x)
exit(y)
