# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/dct_ops_test.py
"""Computes the DCT-I manually with NumPy."""
# X_k = (x_0 + (-1)**k * x_{N-1} +
#       2 * sum_{n=0}^{N-2} x_n * cos(\frac{pi}{N-1} * n * k)  k=0,...,N-1
del norm
signals_mod = _modify_input_for_dct(signals, n=n)
dct_size = signals_mod.shape[-1]
dct = np.zeros_like(signals_mod)
for k in range(dct_size):
    phi = np.cos(np.pi * np.arange(1, dct_size - 1) * k / (dct_size - 1))
    dct[..., k] = 2 * np.sum(
        signals_mod[..., 1:-1] * phi, axis=-1) + (
            signals_mod[..., 0] + (-1)**k * signals_mod[..., -1])
exit(dct)
