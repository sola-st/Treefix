# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
if np_rtype == np.float32:
    tol = 1e-5
else:
    if window_type == "kaiser_bessel_derived":
        tol = 1e-6
    else:
        tol = 1e-8
    # Generate a random white Gaussian signal.
signal = np.random.normal(size=signal_length).astype(np_rtype)
if window_type == "vorbis":
    window_fn = window_ops.vorbis_window
elif window_type == "kaiser_bessel_derived":
    window_fn = window_ops.kaiser_bessel_derived_window
elif window_type is None:
    window_fn = None
mdct = spectral_ops.mdct(signal, frame_length, norm=norm,
                         window_fn=window_fn, pad_end=pad_end)
inverse_mdct = spectral_ops.inverse_mdct(mdct, norm=norm,
                                         window_fn=window_fn)
inverse_mdct = self.evaluate(inverse_mdct)

# Truncate signal and inverse_mdct to their minimum length.
min_length = np.minimum(signal.shape[0], inverse_mdct.shape[0])
# Ignore the half_len samples at either edge.
half_len = frame_length // 2
signal = signal[half_len:min_length-half_len]
inverse_mdct = inverse_mdct[half_len:min_length-half_len]

# Check that the inverse and original signal are close.
self.assertAllClose(inverse_mdct, signal, atol=tol, rtol=tol)
