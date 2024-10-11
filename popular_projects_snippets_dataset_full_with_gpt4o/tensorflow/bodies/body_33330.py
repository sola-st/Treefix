# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
"""Spectrum for d-dimensional real/symmetric circulant."""
grid_shape = spectrum_shape[-d:]

if grid_shape == (0,) * d:
    kernel = array_ops.reshape(math_ops.cast([], dtype), grid_shape)
else:
    kernel = exponential_power_convolution_kernel(
        grid_shape=grid_shape,
        # power=2 with this scale and no inflation will have some negative
        # spectra. It will still be real/symmetric.
        length_scale=math_ops.cast([0.2] * d, dtype.real_dtype),
        power=1 if ensure_self_adjoint_and_pd else 2,
        zero_inflation=0.2 if ensure_self_adjoint_and_pd else None,
    )
spectrum = linear_operator_circulant._FFT_OP[d](_to_complex(kernel))
spectrum = math_ops.cast(spectrum, dtype)
exit(array_ops.broadcast_to(spectrum, spectrum_shape))
