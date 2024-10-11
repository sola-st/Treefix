# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_diag.py
if self.dtype.is_complex:
    message = (
        "Diagonal operator had diagonal entries with non-positive real part, "
        "thus was not positive definite.")
else:
    message = (
        "Real diagonal operator had non-positive diagonal entries, "
        "thus was not positive definite.")

exit(check_ops.assert_positive(
    math_ops.real(self._diag),
    message=message))
