# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
# If there is only one coefficient, the formula still works, and we get one
# as the answer, always.
x_a = [5.5]
x_b = [0.1]
with self.session():
    self.assertAllClose(
        1,
        self.evaluate(math_ops.exp(special_math_ops.lbeta(x_a))),
        rtol=3e-6)
    self.assertAllClose(
        1, self.evaluate(math_ops.exp(special_math_ops.lbeta(x_b))))
    self.assertEqual((), special_math_ops.lbeta(x_a).get_shape())
