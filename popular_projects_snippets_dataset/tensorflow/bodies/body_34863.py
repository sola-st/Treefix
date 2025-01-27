# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
with self.cached_session():
    alpha = np.random.rand(3, 2, 2)
    n = [[3., 2], [4, 5], [6, 7]]
    dist = ds.DirichletMultinomial(n, alpha)
    self.assertEqual(2, dist.event_shape_tensor().eval())
    self.assertAllEqual([3, 2], dist.batch_shape_tensor())
    self.assertEqual(tensor_shape.TensorShape([2]), dist.event_shape)
    self.assertEqual(tensor_shape.TensorShape([3, 2]), dist.batch_shape)
