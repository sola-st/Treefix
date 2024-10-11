# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/mfcc_ops_test.py
# num_mel_bins must be positive.
with self.assertRaises(ValueError):
    signal = array_ops.zeros((2, 3, 0))
    mfcc_ops.mfccs_from_log_mel_spectrograms(signal)
