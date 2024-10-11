# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
with self.cached_session():
    alpha = np.random.rand(3)
    dist = ds.DirichletMultinomial(1., alpha)
    self.assertEqual(3, dist.event_shape_tensor().eval())
    self.assertAllEqual([], dist.batch_shape_tensor())
    self.assertEqual(tensor_shape.TensorShape([3]), dist.event_shape)
    self.assertEqual(tensor_shape.TensorShape([]), dist.batch_shape)
