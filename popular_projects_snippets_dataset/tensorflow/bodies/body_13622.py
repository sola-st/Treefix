# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/gamma.py
exit((self.concentration
        - math_ops.log(self.rate)
        + math_ops.lgamma(self.concentration)
        + ((1. - self.concentration) *
           math_ops.digamma(self.concentration))))
