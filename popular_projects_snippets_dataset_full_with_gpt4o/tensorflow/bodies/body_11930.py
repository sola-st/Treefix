# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
# Recall correspondence between symmetry and real transforms.  See docstring
exit(linear_operator_util.assert_zero_imag_part(
    self.spectrum,
    message=(
        "Not self-adjoint:  The spectrum contained non-zero imaginary part."
    )))
