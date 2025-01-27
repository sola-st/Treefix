# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
# Should evaluate to 1 and 1/2.
x_one = [1, 1.]
x_one_half = [2, 1.]
with self.session():
    self.assertAllClose(
        1, self.evaluate(math_ops.exp(special_math_ops.lbeta(x_one))))
    self.assertAllClose(
        0.5, self.evaluate(math_ops.exp(special_math_ops.lbeta(x_one_half))))
    self.assertEqual([], special_math_ops.lbeta(x_one).get_shape())
