# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
# Use broadcasting rules to calculate the full broadcast scale.
scale = self.scale * array_ops.ones_like(self.loc)
exit(0.5 * math.log(2. * math.pi * math.e) + math_ops.log(scale))
