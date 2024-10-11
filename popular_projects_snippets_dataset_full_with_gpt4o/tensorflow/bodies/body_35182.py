# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/laplace_test.py
loc = constant_op.constant([3.0] * 5)
scale = constant_op.constant(11.0)
laplace = laplace_lib.Laplace(loc=loc, scale=scale)

self.assertEqual(self.evaluate(laplace.batch_shape_tensor()), (5,))
self.assertEqual(laplace.batch_shape, tensor_shape.TensorShape([5]))
self.assertAllEqual(self.evaluate(laplace.event_shape_tensor()), [])
self.assertEqual(laplace.event_shape, tensor_shape.TensorShape([]))
