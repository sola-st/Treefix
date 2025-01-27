# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/dct_ops_test.py
"""Compares (I)DCT to SciPy (if available) and a NumPy implementation."""
np_dct = NP_DCT[dct_type](signals, n=n, norm=norm)
tf_dct = dct_ops.dct(signals, n=n, type=dct_type, norm=norm)
self.assertEqual(tf_dct.dtype.as_numpy_dtype, signals.dtype)
self.assertAllClose(np_dct, tf_dct, atol=atol, rtol=rtol)
np_idct = NP_IDCT[dct_type](signals, n=None, norm=norm)
tf_idct = dct_ops.idct(signals, type=dct_type, norm=norm)
self.assertEqual(tf_idct.dtype.as_numpy_dtype, signals.dtype)
self.assertAllClose(np_idct, tf_idct, atol=atol, rtol=rtol)
if fftpack and dct_type != 4:
    scipy_dct = fftpack.dct(signals, n=n, type=dct_type, norm=norm)
    self.assertAllClose(scipy_dct, tf_dct, atol=atol, rtol=rtol)
    scipy_idct = fftpack.idct(signals, type=dct_type, norm=norm)
    self.assertAllClose(scipy_idct, tf_idct, atol=atol, rtol=rtol)
# Verify inverse(forward(s)) == s, up to a normalization factor.
# Since `n` is not implemented for IDCT operation, re-calculating tf_dct
# without n.
tf_dct = dct_ops.dct(signals, type=dct_type, norm=norm)
tf_idct_dct = dct_ops.idct(tf_dct, type=dct_type, norm=norm)
tf_dct_idct = dct_ops.dct(tf_idct, type=dct_type, norm=norm)
if norm is None:
    if dct_type == 1:
        tf_idct_dct *= 0.5 / (signals.shape[-1] - 1)
        tf_dct_idct *= 0.5 / (signals.shape[-1] - 1)
    else:
        tf_idct_dct *= 0.5 / signals.shape[-1]
        tf_dct_idct *= 0.5 / signals.shape[-1]
self.assertAllClose(signals, tf_idct_dct, atol=atol, rtol=rtol)
self.assertAllClose(signals, tf_dct_idct, atol=atol, rtol=rtol)
