# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
tol = 1e-4 if np_type == np.float32 else 1e-10
dims = rank + extra_dims
re = np.ones(shape=(4,) * dims, dtype=np_type) / 10.0
im = np.zeros(shape=(4,) * dims, dtype=np_type)
self._check_grad_complex(self._tf_fft_for_rank(rank), re, im,
                         rtol=tol, atol=tol)
self._check_grad_complex(self._tf_ifft_for_rank(rank), re, im,
                         rtol=tol, atol=tol)
