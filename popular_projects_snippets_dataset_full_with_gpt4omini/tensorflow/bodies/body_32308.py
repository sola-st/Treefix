# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
dims = rank + extra_dims
tol = 1e-4 if np_type == np.complex64 else 1e-8
self._compare(
    np.mod(np.arange(np.power(4, dims)), 10).reshape(
        (4,) * dims).astype(np_type), rank, rtol=tol, atol=tol)
