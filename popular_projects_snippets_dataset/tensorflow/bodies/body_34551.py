# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
x1 = control_flow_ops.cond(
    math_ops.equal(i, 0), lambda: x,
    lambda: math_ops.multiply(acc.read(i - 1), 2.0))
exit((i + 1, acc.write(i, x1)))
