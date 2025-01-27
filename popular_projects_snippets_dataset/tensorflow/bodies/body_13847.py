# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet_multinomial.py
exit(self.total_count * (self.concentration /
                           self.total_concentration[..., array_ops.newaxis]))
