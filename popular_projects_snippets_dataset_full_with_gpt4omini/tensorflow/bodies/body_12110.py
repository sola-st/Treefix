# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
with self.session():
    event_size = 0
    for batch_size in [0, 1, 2]:
        x = constant_op.constant([], shape=[batch_size, event_size])
        lbeta_x = special_math_ops.lbeta(x)
        expected_result = constant_op.constant(-np.inf, shape=[batch_size])

        self.assertAllEqual(self.evaluate(expected_result),
                            self.evaluate(lbeta_x))
        self.assertEqual(expected_result.get_shape(), lbeta_x.get_shape())
