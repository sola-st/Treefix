# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
signal = np.zeros((512,)).astype(np.float32)

# If fft_length is not provided, the smallest enclosing power of 2 of
# frame_length (8) is used.
stft = spectral_ops.stft(signal, frame_length=7, frame_step=8,
                         pad_end=True)
self.assertAllEqual([64, 5], stft.shape.as_list())
self.assertAllEqual([64, 5], self.evaluate(stft).shape)

stft = spectral_ops.stft(signal, frame_length=8, frame_step=8,
                         pad_end=True)
self.assertAllEqual([64, 5], stft.shape.as_list())
self.assertAllEqual([64, 5], self.evaluate(stft).shape)

stft = spectral_ops.stft(signal, frame_length=8, frame_step=8,
                         fft_length=16, pad_end=True)
self.assertAllEqual([64, 9], stft.shape.as_list())
self.assertAllEqual([64, 9], self.evaluate(stft).shape)

stft = spectral_ops.stft(signal, frame_length=16, frame_step=8,
                         fft_length=8, pad_end=True)
self.assertAllEqual([64, 5], stft.shape.as_list())
self.assertAllEqual([64, 5], self.evaluate(stft).shape)

stft = np.zeros((32, 9)).astype(np.complex64)

inverse_stft = spectral_ops.inverse_stft(stft, frame_length=8,
                                         fft_length=16, frame_step=8)
expected_length = (stft.shape[0] - 1) * 8 + 8
self.assertAllEqual([256], inverse_stft.shape.as_list())
self.assertAllEqual([expected_length], self.evaluate(inverse_stft).shape)
