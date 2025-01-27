# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_diag.py
exit(linear_operator_util.assert_zero_imag_part(
    self._diag,
    message=(
        "This diagonal operator contained non-zero imaginary values.  "
        " Thus it was not self-adjoint.")))
