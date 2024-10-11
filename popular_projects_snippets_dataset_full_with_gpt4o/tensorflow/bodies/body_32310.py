# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
if context.executing_eagerly():
    exit()
tol = 1e-4 if np_type == np.complex64 else 1e-8
dims = rank + extra_dims
self._compare(
    np.mod(np.arange(np.power(4, dims)), 10).reshape(
        (4,) * dims).astype(np_type),
    rank, use_placeholder=True, rtol=tol, atol=tol)
