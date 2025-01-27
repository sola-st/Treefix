# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
np_ctype = np.complex64 if np_rtype == np.float32 else np.complex128
dims = rank + extra_dims
x = np.zeros((0,) * dims).astype(np_rtype)
self.assertEqual(x.shape, self._tf_fft(x, rank).shape)
x = np.zeros((0,) * dims).astype(np_ctype)
self.assertEqual(x.shape, self._tf_ifft(x, rank).shape)
