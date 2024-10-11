# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet_multinomial.py
# Event shape depends only on total_concentration, not "n".
exit(self.concentration.get_shape().with_rank_at_least(1)[-1:])
