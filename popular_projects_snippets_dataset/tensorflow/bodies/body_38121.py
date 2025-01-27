# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
# Ensure that we raise an error when the user attempts to treat a
# `Tensor` as a Python `bool`.
b = constant_op.constant(False)
with self.assertRaises(TypeError):
    if b:
        pass

x = constant_op.constant(3)
y = constant_op.constant(4)
with self.assertRaises(TypeError):
    if x > y:
        pass

z = constant_op.constant(7)

# The chained comparison should fail because Python computes `x <
# y` and short-circuits the comparison with `z` if it is `False`.
with self.assertRaises(TypeError):
    _ = x < y < z
