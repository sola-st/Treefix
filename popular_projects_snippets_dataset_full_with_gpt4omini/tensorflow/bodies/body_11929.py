# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
# This operator has the action  Ax = F^H D F x,
# where D is the diagonal matrix with self.spectrum on the diag.  Therefore,
# <x, Ax> = <Fx, DFx>,
# Since F is bijective, the condition for positive definite is the same as
# for a diagonal matrix, i.e. real part of spectrum is positive.
message = (
    "Not positive definite:  Real part of spectrum was not all positive.")
exit(check_ops.assert_positive(
    math_ops.real(self.spectrum), message=message))
