# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
del ensure_self_adjoint_and_pd
shape = shape_info.shape
# Will be well conditioned enough to get accurate solves.
spectrum = linear_operator_test_util.random_sign_uniform(
    shape=self._shape_to_spectrum_shape(shape),
    dtype=dtype,
    minval=1.,
    maxval=2.)

lin_op_spectrum = spectrum

if use_placeholder:
    lin_op_spectrum = array_ops.placeholder_with_default(spectrum, shape=None)

operator = linalg.LinearOperatorCirculant(
    lin_op_spectrum, input_output_dtype=dtype)

self.assertEqual(
    operator.parameters,
    {
        "input_output_dtype": dtype,
        "is_non_singular": None,
        "is_positive_definite": None,
        "is_self_adjoint": None,
        "is_square": True,
        "name": "LinearOperatorCirculant",
        "spectrum": lin_op_spectrum,
    })

mat = self._spectrum_to_circulant_1d(spectrum, shape, dtype=dtype)

exit((operator, mat))
