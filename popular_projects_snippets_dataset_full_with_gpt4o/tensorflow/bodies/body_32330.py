# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
"""Test padding (FFT size > dimensions)."""
np_ctype = np.complex64 if np_rtype == np.float32 else np.complex128
tol = 1e-4 if np_rtype == np.float32 else 8e-5
dims = rank + extra_dims
inner_dim = size // 2 + 1
r2c = np.mod(np.arange(np.power(size, dims)), 10).reshape(
    (size,) * dims)
c2r = np.mod(np.arange(np.power(size, dims - 1) * inner_dim),
             10).reshape((size,) * (dims - 1) + (inner_dim,))
fft_length = (size + 2,) * rank
self._compare_forward(r2c.astype(np_rtype), rank, fft_length,
                      rtol=tol, atol=tol)
c2r = self._generate_valid_irfft_input(c2r, np_ctype, r2c, np_rtype, rank,
                                       fft_length)
self._compare_backward(c2r.astype(np_ctype), rank, fft_length,
                       rtol=tol, atol=tol)
# Confirm it works with unknown shapes as well.
if not context.executing_eagerly():
    self._compare_forward(
        r2c.astype(np_rtype),
        rank,
        fft_length,
        use_placeholder=True,
        rtol=tol, atol=tol)
    self._compare_backward(
        c2r.astype(np_ctype),
        rank,
        fft_length,
        use_placeholder=True,
        rtol=tol, atol=tol)
