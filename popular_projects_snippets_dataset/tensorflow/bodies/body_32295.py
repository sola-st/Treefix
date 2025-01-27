# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
x_np = self._np_ifft(x, rank, fft_length)
if use_placeholder:
    x_ph = array_ops.placeholder(dtype=dtypes.as_dtype(x.dtype))
    x_tf = self._tf_ifft(x_ph, rank, fft_length, feed_dict={x_ph: x})
else:
    x_tf = self._tf_ifft(x, rank, fft_length)

self.assertAllClose(x_np, x_tf, rtol=rtol, atol=atol)
