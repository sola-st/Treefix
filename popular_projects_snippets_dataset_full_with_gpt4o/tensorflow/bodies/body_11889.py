# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_tridiag.py
# Check the diagonal has non-zero imaginary, and the super and subdiagonals
# are conjugate.

asserts = []
diag_message = (
    'This tridiagonal operator contained non-zero '
    'imaginary values on the diagonal.')
off_diag_message = (
    'This tridiagonal operator has non-conjugate '
    'subdiagonal and superdiagonal.')

if self.diagonals_format == _MATRIX:
    asserts += [check_ops.assert_equal(
        self.diagonals, linalg.adjoint(self.diagonals),
        message='Matrix was not equal to its adjoint.')]
elif self.diagonals_format == _COMPACT:
    diagonals = ops.convert_to_tensor_v2_with_dispatch(self.diagonals)
    asserts += [linear_operator_util.assert_zero_imag_part(
        diagonals[..., 1, :], message=diag_message)]
    # Roll the subdiagonal so the shifted argument is at the end.
    subdiag = manip_ops.roll(diagonals[..., 2, :], shift=-1, axis=-1)
    asserts += [check_ops.assert_equal(
        math_ops.conj(subdiag[..., :-1]),
        diagonals[..., 0, :-1],
        message=off_diag_message)]
else:
    asserts += [linear_operator_util.assert_zero_imag_part(
        self.diagonals[1], message=diag_message)]
    subdiag = manip_ops.roll(self.diagonals[2], shift=-1, axis=-1)
    asserts += [check_ops.assert_equal(
        math_ops.conj(subdiag[..., :-1]),
        self.diagonals[0][..., :-1],
        message=off_diag_message)]
exit(control_flow_ops.group(asserts))
