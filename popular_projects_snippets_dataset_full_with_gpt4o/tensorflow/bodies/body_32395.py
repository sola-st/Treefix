# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/dct_ops_test.py
"""Computes the DCT-II manually with NumPy."""
# X_k = sum_{n=0}^{N-1} x_n * cos(\frac{pi}{N} * (n + 0.5) * k)  k=0,...,N-1
signals_mod = _modify_input_for_dct(signals, n=n)
dct_size = signals_mod.shape[-1]
dct = np.zeros_like(signals_mod)
for k in range(dct_size):
    phi = np.cos(np.pi * (np.arange(dct_size) + 0.5) * k / dct_size)
    dct[..., k] = np.sum(signals_mod * phi, axis=-1)
# SciPy's `dct` has a scaling factor of 2.0 which we follow.
# https://github.com/scipy/scipy/blob/v1.2.1/scipy/fftpack/src/dct.c.src
if norm == "ortho":
    # The orthonormal scaling includes a factor of 0.5 which we combine with
    # the overall scaling of 2.0 to cancel.
    dct[..., 0] *= np.sqrt(1.0 / dct_size)
    dct[..., 1:] *= np.sqrt(2.0 / dct_size)
else:
    dct *= 2.0
exit(dct)
