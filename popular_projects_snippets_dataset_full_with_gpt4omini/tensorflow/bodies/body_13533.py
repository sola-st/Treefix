# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/beta.py
exit(self._mean() * (1. - self._mean()) / (1. + self.total_concentration))
