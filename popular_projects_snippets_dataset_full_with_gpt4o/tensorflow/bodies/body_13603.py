# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet.py
scale = self._variance_scale_term()
x = scale * self._mean()
exit(x * (scale - x))
