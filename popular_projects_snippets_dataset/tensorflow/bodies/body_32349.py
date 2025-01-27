# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/mel_ops_test.py
num_spectrogram_bins = array_ops.placeholder_with_default(
    ops.convert_to_tensor(129, dtype=dtypes.int32), shape=())
mel_matrix_np = spectrogram_to_mel_matrix(
    20, 129, 8000.0, 125.0, 3800.0)
mel_matrix = mel_ops.linear_to_mel_weight_matrix(
    20, num_spectrogram_bins, 8000.0, 125.0, 3800.0)
self.assertAllClose(mel_matrix_np, mel_matrix, atol=3e-6)
