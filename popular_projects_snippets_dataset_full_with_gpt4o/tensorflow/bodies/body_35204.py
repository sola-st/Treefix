# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = np.random.rand(3, 2, 2)
dist = dirichlet_lib.Dirichlet(alpha)
self.assertEqual(2, self.evaluate(dist.event_shape_tensor()))
self.assertAllEqual([3, 2], self.evaluate(dist.batch_shape_tensor()))
self.assertEqual(tensor_shape.TensorShape([2]), dist.event_shape)
self.assertEqual(tensor_shape.TensorShape([3, 2]), dist.batch_shape)
