# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
# dy/dx = dy/dy * dy/dx = 1.0 * (6x^2+6x+4)
exit(functional_ops.Gradient([x, 1.0], Poly)[0])
