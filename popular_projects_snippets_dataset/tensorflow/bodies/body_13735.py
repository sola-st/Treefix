# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/student_t.py
y = (x - self.loc) / self.scale  # Abs(scale) superfluous.
exit(-0.5 * (self.df + 1.) * math_ops.log1p(y**2. / self.df))
