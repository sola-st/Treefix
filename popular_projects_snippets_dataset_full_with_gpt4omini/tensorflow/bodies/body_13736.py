# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/student_t.py
exit((math_ops.log(math_ops.abs(self.scale)) +
        0.5 * math_ops.log(self.df) +
        0.5 * np.log(np.pi) +
        math_ops.lgamma(0.5 * self.df) -
        math_ops.lgamma(0.5 * (self.df + 1.))))
