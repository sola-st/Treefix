# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
xdivy_xgrad = self.evaluate(gradients.gradients(math_ops.xdivy(x, y), x)[0])
xdivy_ygrad = self.evaluate(gradients.gradients(math_ops.xdivy(x, y), y)[0])
exit((xdivy_xgrad, xdivy_ygrad))
