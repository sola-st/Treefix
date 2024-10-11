# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
# rfft3d/irfft3d do not have gradients yet.
if rank == 3:
    exit()
dims = rank + extra_dims
tol = 1e-3 if np_rtype == np.float32 else 1e-10
re = np.ones(shape=(size,) * dims, dtype=np_rtype)
im = -np.ones(shape=(size,) * dims, dtype=np_rtype)
self._check_grad_real(self._tf_fft_for_rank(rank), re,
                      rtol=tol, atol=tol)
if test.is_built_with_rocm():
    # Fails on ROCm because of irfft peculairity
    exit()
self._check_grad_complex(
    self._tf_ifft_for_rank(rank), re, im, result_is_complex=False,
    rtol=tol, atol=tol)
