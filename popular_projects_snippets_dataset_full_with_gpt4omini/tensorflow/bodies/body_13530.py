# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/beta.py
exit((math_ops.lgamma(self.concentration1)
        + math_ops.lgamma(self.concentration0)
        - math_ops.lgamma(self.total_concentration)))
