# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/laplace.py
z = self._z(x)
exit((0.5 + 0.5 * math_ops.sign(z) *
        (1. - math_ops.exp(-math_ops.abs(z)))))
