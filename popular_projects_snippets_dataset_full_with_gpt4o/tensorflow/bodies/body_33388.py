# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
spectrum = variables_module.Variable(
    math_ops.cast([[1. + 0j, 1. + 0j], [1. + 1j, 2. + 2j]],
                  dtypes.complex64))
operator = linalg.LinearOperatorCirculant2D(spectrum)
self.check_tape_safe(operator)
