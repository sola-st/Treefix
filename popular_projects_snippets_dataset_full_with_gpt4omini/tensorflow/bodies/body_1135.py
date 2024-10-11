# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py
ws = 512
hs = 128
dims = (ws * 20,)
shape = BATCH_DIMS + dims
data = np.arange(np.prod(shape)) / np.prod(dims)
np.random.seed(123)
np.random.shuffle(data)
data = np.reshape(data.astype(np.float32), shape)
window = sps.get_window("hann", ws)
expected = sps.stft(
    data, nperseg=ws, noverlap=ws - hs, boundary=None, window=window)[2]
expected = np.swapaxes(expected, -1, -2)
expected *= window.sum()  # scipy divides by window sum
with self.session() as sess:
    with self.test_scope():
        ph = array_ops.placeholder(
            dtypes.as_dtype(data.dtype), shape=data.shape)
        out = signal.stft(ph, ws, hs)
        grad = gradients_impl.gradients(out, ph,
                                        grad_ys=array_ops.ones_like(out))

    # For gradients, we simply verify that they compile & execute.
    value, _ = sess.run([out, grad], {ph: data})
    self.assertAllClose(expected, value, rtol=RTOL, atol=ATOL)
