# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
real = math_ops.cos(x)
imag = ops.convert_to_tensor(1.)
exit(math_ops.abs(math_ops.complex(real, imag)))
