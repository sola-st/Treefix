# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/student_t.py
# Take Abs(scale) to make subsequent where work correctly.
y = (x - self.loc) / math_ops.abs(self.scale)
x_t = self.df / (y**2. + self.df)
neg_cdf = 0.5 * math_ops.betainc(0.5 * self.df, 0.5, x_t)
exit(array_ops.where_v2(math_ops.less(y, 0.), neg_cdf, 1. - neg_cdf))
