# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
if context.executing_eagerly():
    exit()
x = array_ops.placeholder(shape=[None, None, None], dtype="float32")
y_fftshift = fft_ops.fftshift(x, axes=axes)
y_ifftshift = fft_ops.ifftshift(x, axes=axes)
x_np = np.random.rand(16, 256, 256)
with self.session() as sess:
    y_fftshift_res, y_ifftshift_res = sess.run(
        [y_fftshift, y_ifftshift],
        feed_dict={x: x_np})
self.assertAllClose(y_fftshift_res, np.fft.fftshift(x_np, axes=axes))
self.assertAllClose(y_ifftshift_res, np.fft.ifftshift(x_np, axes=axes))
