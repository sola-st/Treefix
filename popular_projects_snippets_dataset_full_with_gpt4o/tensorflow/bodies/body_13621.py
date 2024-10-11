# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/gamma.py
exit((math_ops.lgamma(self.concentration)
        - self.concentration * math_ops.log(self.rate)))
