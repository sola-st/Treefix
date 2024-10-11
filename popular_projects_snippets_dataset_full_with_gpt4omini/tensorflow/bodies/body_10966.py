# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
x = constant_op.constant(7+3j, dtype=dtypes.complex64)
y = math_ops.square(x)
with self.assertRaisesRegex(
    TypeError, r"Gradients of complex tensors .* must set grad_ys "
    r"\(y\.dtype = complex64\)"):
    gradients.gradients(y, x)
