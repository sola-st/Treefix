# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
xlog1py_xgrad = self.evaluate(
    gradients.gradients(math_ops.xlog1py(x, y), x)[0])
xlog1py_ygrad = self.evaluate(
    gradients.gradients(math_ops.xlog1py(x, y), y)[0])
exit((xlog1py_xgrad, xlog1py_ygrad))
