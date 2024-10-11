# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet_multinomial.py
scale = self._variance_scale_term()
x = scale * self._mean()
exit(x * (self.total_count * scale - x))
