# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
# Should evaluate to 1/2.
x_one_half = [[2, 1.], [2, 1.]]
with self.session():
    self.assertAllClose(
        [0.5, 0.5],
        self.evaluate(math_ops.exp(special_math_ops.lbeta(x_one_half))))
    self.assertEqual(
        (2,),
        self.evaluate(array_ops.shape(special_math_ops.lbeta(x_one_half))))
    self.assertEqual(
        tensor_shape.TensorShape([2]),
        special_math_ops.lbeta(x_one_half).get_shape())
