# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
mu = array_ops.placeholder(dtype=dtypes.float32)
sigma = array_ops.placeholder(dtype=dtypes.float32)
normal = normal_lib.Normal(loc=mu, scale=sigma)

with self.cached_session() as sess:
    # get_batch_shape should return an "<unknown>" tensor.
    self.assertEqual(normal.batch_shape, tensor_shape.TensorShape(None))
    self.assertEqual(normal.event_shape, ())
    self.assertAllEqual(self.evaluate(normal.event_shape_tensor()), [])
    self.assertAllEqual(
        sess.run(normal.batch_shape_tensor(),
                 feed_dict={mu: 5.0,
                            sigma: [1.0, 2.0]}), [2])
