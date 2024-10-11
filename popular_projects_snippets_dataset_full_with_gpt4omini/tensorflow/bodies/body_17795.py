# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
with self.cached_session() as sess:
    x = array_ops.placeholder(dtypes.float32)
    y = array_ops.concat([x, x], axis=0)
    jacobian = gradients.batch_jacobian(y, x)
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "assertion failed"):
        sess.run(jacobian, feed_dict={x: [[1, 2], [3, 4]]})
