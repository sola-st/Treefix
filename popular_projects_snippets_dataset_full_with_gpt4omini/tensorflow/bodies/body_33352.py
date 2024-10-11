# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
spectrum = variables_module.Variable(
    math_ops.cast([1. + 0j, 1. + 1j], dtypes.complex64))
operator = linalg.LinearOperatorCirculant(spectrum, is_self_adjoint=False)
self.check_tape_safe(operator)
