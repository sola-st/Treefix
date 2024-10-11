# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/laplace.py
# Use broadcasting rules to calculate the full broadcast scale.
scale = self.scale + array_ops.zeros_like(self.loc)
exit(math.log(2.) + 1. + math_ops.log(scale))
