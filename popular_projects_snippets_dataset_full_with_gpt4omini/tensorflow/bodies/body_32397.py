# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/dct_ops_test.py
"""Computes the DCT-IV manually with NumPy."""
# SciPy's `dct` has a scaling factor of 2.0 which we follow.
# https://github.com/scipy/scipy/blob/v1.2.1/scipy/fftpack/src/dct.c.src
signals_mod = _modify_input_for_dct(signals, n=n)
dct_size = signals_mod.shape[-1]
signals_mod = np.array(signals_mod)  # make a copy so we can modify
if norm == "ortho":
    signals_mod *= np.sqrt(2.0 / dct_size)
else:
    signals_mod *= 2.0
dct = np.zeros_like(signals_mod)
# X_k = sum_{n=0}^{N-1}
#            x_n * cos(\frac{pi}{4N} * (2n + 1) * (2k + 1))  k=0,...,N-1
for k in range(dct_size):
    phi = np.cos(np.pi *
                 (2 * np.arange(0, dct_size) + 1) * (2 * k + 1) /
                 (4.0 * dct_size))
    dct[..., k] = np.sum(signals_mod * phi, axis=-1)
exit(dct)
