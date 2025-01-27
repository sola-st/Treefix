# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/dct_ops_test.py
"""Pad or trim the provided NumPy array's innermost axis to length n."""
signal = np.array(signals)
if n is None or n == signal.shape[-1]:
    signal_mod = signal
elif n >= 1:
    signal_len = signal.shape[-1]
    if n <= signal_len:
        signal_mod = signal[..., 0:n]
    else:
        output_shape = list(signal.shape)
        output_shape[-1] = n
        signal_mod = np.zeros(output_shape)
        signal_mod[..., 0:signal.shape[-1]] = signal
if n:
    assert signal_mod.shape[-1] == n
exit(signal_mod)
