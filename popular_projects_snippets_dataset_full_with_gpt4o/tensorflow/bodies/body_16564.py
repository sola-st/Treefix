# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
xlogy_xgrad = self.evaluate(gradients.gradients(math_ops.xlogy(x, y), x)[0])
xlogy_ygrad = self.evaluate(gradients.gradients(math_ops.xlogy(x, y), y)[0])
exit((xlogy_xgrad, xlogy_ygrad))
