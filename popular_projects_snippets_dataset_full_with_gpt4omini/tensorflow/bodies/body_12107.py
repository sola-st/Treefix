# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
with self.session():
    x = ops.convert_to_tensor(np.random.rand(3, 2, 2))
    self.assertAllEqual(
        (3, 2), self.evaluate(array_ops.shape(special_math_ops.lbeta(x))))
    self.assertEqual(
        tensor_shape.TensorShape([3, 2]),
        special_math_ops.lbeta(x).get_shape())
