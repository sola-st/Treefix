# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
with self.cached_session():
    p = 0.5 * np.ones([3, 2, 2], dtype=np.float32)
    n = [[3., 2], [4, 5], [6, 7]]
    dist = multinomial.Multinomial(total_count=n, probs=p)
    self.assertEqual(2, dist.event_shape_tensor().eval())
    self.assertAllEqual([3, 2], dist.batch_shape_tensor())
    self.assertEqual(tensor_shape.TensorShape([2]), dist.event_shape)
    self.assertEqual(tensor_shape.TensorShape([3, 2]), dist.batch_shape)
