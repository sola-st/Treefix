# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
# Verify that concat doesn't crash and burn for zero size inputs
np.random.seed(7)
with test_util.use_gpu():
    for shape0 in (), (2,):
        axis = len(shape0)
        for shape1 in (), (3,):
            for n0 in 0, 1, 2:
                for n1 in 0, 1, 2:
                    x0 = np.random.randn(*(shape0 + (n0,) + shape1))
                    x1 = np.random.randn(*(shape0 + (n1,) + shape1))
                    correct = np.concatenate([x0, x1], axis=axis)
                    # TODO(irving): Make tf.concat handle map, then drop list().
                    xs = list(map(constant_op.constant, [x0, x1]))
                    c = array_ops.concat(xs, axis)
                    self.assertAllEqual(self.evaluate(c), correct)
                    # Check gradients
                    dc = np.random.randn(*c.get_shape().as_list())
                    dxs = self.evaluate(gradients_impl.gradients(c, xs, dc))
                    self.assertAllEqual(dc, np.concatenate(dxs, axis=axis))
