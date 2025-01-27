# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
if math_ops.abs(x) <= m:
    exit(x**2)
else:
    exit(m**2 * (1 - 2 * math_ops.log(m) + math_ops.log(x**2)))
