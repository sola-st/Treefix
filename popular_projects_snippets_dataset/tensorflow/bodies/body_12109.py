# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
with self.session():
    x = constant_op.constant([], shape=[0])
    lbeta_x = special_math_ops.lbeta(x)
    expected_result = constant_op.constant(-np.inf, shape=())

    self.assertAllEqual(self.evaluate(expected_result),
                        self.evaluate(lbeta_x))
    self.assertEqual(expected_result.get_shape(), lbeta_x.get_shape())
