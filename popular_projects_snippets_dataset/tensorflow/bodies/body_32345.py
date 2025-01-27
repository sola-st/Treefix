# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/mel_ops_test.py
if use_tensor_sample_rate:
    sample_rate = constant_op.constant(sample_rate)
mel_matrix_np = spectrogram_to_mel_matrix(
    num_mel_bins, num_spectrogram_bins, sample_rate, lower_edge_hertz,
    upper_edge_hertz, dtype)
mel_matrix = mel_ops.linear_to_mel_weight_matrix(
    num_mel_bins, num_spectrogram_bins, sample_rate, lower_edge_hertz,
    upper_edge_hertz, dtype)
self.assertAllClose(mel_matrix_np, mel_matrix, atol=3e-6)
