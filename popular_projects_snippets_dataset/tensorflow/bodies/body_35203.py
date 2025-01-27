# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = np.random.rand(3)
dist = dirichlet_lib.Dirichlet(alpha)
self.assertEqual(3, self.evaluate(dist.event_shape_tensor()))
self.assertAllEqual([], self.evaluate(dist.batch_shape_tensor()))
self.assertEqual(tensor_shape.TensorShape([3]), dist.event_shape)
self.assertEqual(tensor_shape.TensorShape([]), dist.batch_shape)
