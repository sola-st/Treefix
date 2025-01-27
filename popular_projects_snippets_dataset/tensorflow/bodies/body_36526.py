# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
r = control_flow_ops.while_loop(
    lambda _: True,
    lambda x: math_ops.multiply(v, x, name="my_mul"), [1.0],
    maximum_iterations=5,
    name="outer")
exit(array_ops.identity(r))
