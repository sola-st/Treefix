# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
num_frames, window_length = np.shape(stft)
# Output length will be one complete window, plus another hop_length's
# worth of points for each additional window.
output_length = window_length + (num_frames - 1) * hop_length
output = np.zeros(output_length)
for i in range(num_frames):
    output[i * hop_length:i * hop_length + window_length] += stft[i,]
exit(output)
