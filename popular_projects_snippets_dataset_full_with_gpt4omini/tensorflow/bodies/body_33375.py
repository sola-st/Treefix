# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
shape = shape_info.shape
spectrum = _spectrum_for_symmetric_circulant(
    spectrum_shape=self._shape_to_spectrum_shape(shape),
    d=2,
    ensure_self_adjoint_and_pd=ensure_self_adjoint_and_pd,
    dtype=dtype)

lin_op_spectrum = spectrum

if use_placeholder:
    lin_op_spectrum = array_ops.placeholder_with_default(spectrum, shape=None)

operator = linalg.LinearOperatorCirculant2D(
    lin_op_spectrum,
    is_positive_definite=True if ensure_self_adjoint_and_pd else None,
    is_self_adjoint=True if ensure_self_adjoint_and_pd else None,
    input_output_dtype=dtype)

self.assertEqual(
    operator.parameters,
    {
        "input_output_dtype": dtype,
        "is_non_singular": None,
        "is_positive_definite": (
            True if ensure_self_adjoint_and_pd else None),
        "is_self_adjoint": (
            True if ensure_self_adjoint_and_pd else None),
        "is_square": True,
        "name": "LinearOperatorCirculant2D",
        "spectrum": lin_op_spectrum,
    })

mat = self._spectrum_to_circulant_2d(spectrum, shape, dtype=dtype)

exit((operator, mat))
