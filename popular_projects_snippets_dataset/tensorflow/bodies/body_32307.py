# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
dims = rank + extra_dims
x = np.zeros((0,) * dims).astype(np_type)
self.assertEqual(x.shape, self._tf_fft(x, rank).shape)
self.assertEqual(x.shape, self._tf_ifft(x, rank).shape)
