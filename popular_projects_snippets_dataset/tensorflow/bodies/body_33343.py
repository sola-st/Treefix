# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
shape = shape_info.shape
# For this test class, we are creating real spectrums.
# We also want the spectrum to have eigenvalues bounded away from zero.
#
# spectrum is bounded away from zero.
spectrum = linear_operator_test_util.random_sign_uniform(
    shape=self._shape_to_spectrum_shape(shape), minval=1., maxval=2.)
if ensure_self_adjoint_and_pd:
    spectrum = math_ops.abs(spectrum)
# If dtype is complex, cast spectrum to complex.  The imaginary part will be
# zero, so the operator will still be self-adjoint.
spectrum = math_ops.cast(spectrum, dtype)

lin_op_spectrum = spectrum

if use_placeholder:
    lin_op_spectrum = array_ops.placeholder_with_default(spectrum, shape=None)

operator = linalg.LinearOperatorCirculant(
    lin_op_spectrum,
    is_self_adjoint=True,
    is_positive_definite=True if ensure_self_adjoint_and_pd else None,
    input_output_dtype=dtype)

mat = self._spectrum_to_circulant_1d(spectrum, shape, dtype=dtype)

exit((operator, mat))
