# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
mu = constant_op.constant([-3.0] * 5)
sigma = constant_op.constant(11.0)
normal = normal_lib.Normal(loc=mu, scale=sigma)

self.assertEqual(self.evaluate(normal.batch_shape_tensor()), [5])
self.assertEqual(normal.batch_shape, tensor_shape.TensorShape([5]))
self.assertAllEqual(self.evaluate(normal.event_shape_tensor()), [])
self.assertEqual(normal.event_shape, tensor_shape.TensorShape([]))
