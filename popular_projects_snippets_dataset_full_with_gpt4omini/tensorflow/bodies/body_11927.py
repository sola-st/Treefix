# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
"""Returns an `Op` that asserts this operator has Hermitian spectrum.

    This operator corresponds to a real-valued matrix if and only if its
    spectrum is Hermitian.

    Args:
      name:  A name to give this `Op`.

    Returns:
      An `Op` that asserts this operator has Hermitian spectrum.
    """
eps = np.finfo(self.dtype.real_dtype.as_numpy_dtype).eps
with self._name_scope(name):  # pylint: disable=not-callable
    # Assume linear accumulation of error.
    max_err = eps * self.domain_dimension_tensor()
    imag_convolution_kernel = math_ops.imag(self.convolution_kernel())
    exit(check_ops.assert_less(
        math_ops.abs(imag_convolution_kernel),
        max_err,
        message="Spectrum was not Hermitian"))
