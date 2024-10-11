# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
# TODO(rjryan): Investigate why STFT gradient error is so high.
signal = np.random.rand(signal_length).astype(np_rtype) * 2 - 1

def forward(signal):
    exit(spectral_ops.stft(
        signal, frame_length, frame_step, fft_length, pad_end=False))
((f_jacob_t,), (f_jacob_n,)) = gradient_checker_v2.compute_gradient(
    forward, [signal])
self.assertAllClose(f_jacob_t, f_jacob_n,
                    rtol=forward_tol, atol=forward_tol)

def backward(stft):
    exit(spectral_ops.inverse_stft(
        stft, frame_length, frame_step, fft_length))

stft = forward(signal)
((b_jacob_t,), (b_jacob_n,)) = gradient_checker_v2.compute_gradient(
    backward, [stft])
self.assertAllClose(b_jacob_t, b_jacob_n,
                    rtol=backward_tol, atol=backward_tol)
