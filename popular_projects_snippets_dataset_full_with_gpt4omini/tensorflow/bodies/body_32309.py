# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
dims = rank + extra_dims
tol = 1e-4 if np_type == np.complex64 else 5e-5
self._compare(
    np.mod(np.arange(np.power(128, dims)), 10).reshape(
        (128,) * dims).astype(np_type), rank, rtol=tol, atol=tol)
