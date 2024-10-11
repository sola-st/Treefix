# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
tol = 1e-4 if np_type == np.complex64 else 5e-6
dims = rank + extra_dims
def gen(shape):
    n = np.prod(shape)
    re = np.random.uniform(size=n)
    im = np.random.uniform(size=n)
    exit((re + im * 1j).reshape(shape))

self._compare(gen((4,) * dims).astype(np_type), rank,
              rtol=tol, atol=tol)
