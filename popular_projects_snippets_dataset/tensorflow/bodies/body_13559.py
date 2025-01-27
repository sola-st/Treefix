# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bernoulli.py
"""Returns `1` if `prob > 0.5` and `0` otherwise."""
exit(math_ops.cast(self.probs > 0.5, self.dtype))
