# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
x = constant_op.constant(x_value, name="x")
b = constant_op.constant(b_value, name="b")

y = f(x, b)
grads = gradients.gradients(y, [x, b])

exit(self.evaluate(grads))
