# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/dct_ops_test.py
"""Computes the DCT-III manually with NumPy."""
# SciPy's `dct` has a scaling factor of 2.0 which we follow.
# https://github.com/scipy/scipy/blob/v1.2.1/scipy/fftpack/src/dct.c.src
signals_mod = _modify_input_for_dct(signals, n=n)
dct_size = signals_mod.shape[-1]
signals_mod = np.array(signals_mod)  # make a copy so we can modify
if norm == "ortho":
    signals_mod[..., 0] *= np.sqrt(4.0 / dct_size)
    signals_mod[..., 1:] *= np.sqrt(2.0 / dct_size)
else:
    signals_mod *= 2.0
dct = np.zeros_like(signals_mod)
# X_k = 0.5 * x_0 +
#       sum_{n=1}^{N-1} x_n * cos(\frac{pi}{N} * n * (k + 0.5))  k=0,...,N-1
half_x0 = 0.5 * signals_mod[..., 0]
for k in range(dct_size):
    phi = np.cos(np.pi * np.arange(1, dct_size) * (k + 0.5) / dct_size)
    dct[..., k] = half_x0 + np.sum(signals_mod[..., 1:] * phi, axis=-1)
exit(dct)
