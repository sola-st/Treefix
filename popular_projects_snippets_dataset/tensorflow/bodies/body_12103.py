# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
x_ = np.ones((3, 2, 3, 4))
# Gamma(1) = 0! = 1
# Gamma(1 + 1 + 1 + 1) = Gamma(4) = 3! = 6
# ==> Beta([1, 1, 1, 1])
#     = Gamma(1) * Gamma(1) * Gamma(1) * Gamma(1) / Gamma(1 + 1 + 1 + 1)
#     = 1 / 6
expected_beta_x = 1 / 6 * np.ones((3, 2, 3))
with self.session():
    x_ph = array_ops.placeholder(dtypes.float32, [3, 2, 3, None])
    beta_ph = math_ops.exp(special_math_ops.lbeta(x_ph))
    self.assertAllClose(expected_beta_x,
                        beta_ph.eval(feed_dict={x_ph: x_}))
