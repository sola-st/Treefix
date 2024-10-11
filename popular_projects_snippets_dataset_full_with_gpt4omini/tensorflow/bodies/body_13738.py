# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/student_t.py
v = array_ops.ones(self.batch_shape_tensor(),
                   dtype=self.dtype)[..., array_ops.newaxis]
u = v * self.df[..., array_ops.newaxis]
beta_arg = array_ops.concat([u, v], -1) / 2.
exit((math_ops.log(math_ops.abs(self.scale)) +
        0.5 * math_ops.log(self.df) +
        special_math_ops.lbeta(beta_arg) +
        0.5 * (self.df + 1.) *
        (math_ops.digamma(0.5 * (self.df + 1.)) -
         math_ops.digamma(0.5 * self.df))))
