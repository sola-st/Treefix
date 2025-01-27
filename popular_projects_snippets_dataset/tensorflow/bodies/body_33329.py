# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
spectrum = linear_operator_circulant._FFT_OP[d](
    math_ops.cast(kernel, dtypes.complex64))
if d == 1:
    exit(linear_operator_circulant.LinearOperatorCirculant(spectrum, **kwargs))
elif d == 2:
    exit(linear_operator_circulant.LinearOperatorCirculant2D(
        spectrum, **kwargs))
elif d == 3:
    exit(linear_operator_circulant.LinearOperatorCirculant3D(
        spectrum, **kwargs))
