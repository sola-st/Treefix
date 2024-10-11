# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
a = math_ops.tanh(math_ops.matmul(a, ws[i, :]) + bs[i, :])
exit((a, ws, bs))
