# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
"""Numpy implementation of `fill_triangular`."""
x = np.asarray(x)
# Formula derived by solving for n: m = n(n+1)/2.
m = np.int32(x.shape[-1])
n = np.sqrt(0.25 + 2. * m) - 0.5
if n != np.floor(n):
    raise ValueError("Invalid shape.")
n = np.int32(n)
# We can't do: `x[..., -(n**2-m):]` because this doesn't correctly handle
# `m == n == 1`. Hence, we do absolute indexing.
x_tail = x[..., (m - (n * n - m)):]
y = np.concatenate(
    [x, x_tail[..., ::-1]] if upper else [x_tail, x[..., ::-1]],
    axis=-1)
y = y.reshape(np.concatenate([
    np.int32(x.shape[:-1]),
    np.int32([n, n]),
], axis=0))
exit(np.triu(y) if upper else np.tril(y))
