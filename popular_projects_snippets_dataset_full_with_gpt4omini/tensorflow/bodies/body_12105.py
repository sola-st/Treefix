# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
# Should evaluate to 1/2.
x_one_half = [[2, 1.], [2, 1.]]
with self.session():
    ph = array_ops.placeholder(dtypes.float32)
    beta_ph = math_ops.exp(special_math_ops.lbeta(ph))
    self.assertAllClose([0.5, 0.5],
                        beta_ph.eval(feed_dict={ph: x_one_half}))
