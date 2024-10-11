# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
dims = rank + extra_dims
tol = 1e-2 if np_type == np.float32 else 1e-10
re = np.random.rand(*((3,) * dims)).astype(np_type) * 2 - 1
im = np.random.rand(*((3,) * dims)).astype(np_type) * 2 - 1
self._check_grad_complex(self._tf_fft_for_rank(rank), re, im,
                         rtol=tol, atol=tol)
self._check_grad_complex(self._tf_ifft_for_rank(rank), re, im,
                         rtol=tol, atol=tol)
