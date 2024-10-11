# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
with self.cached_session():
    p = [.1, .3, .6]
    dist = multinomial.Multinomial(total_count=1., probs=p)
    self.assertEqual(3, dist.event_shape_tensor().eval())
    self.assertAllEqual([], dist.batch_shape_tensor())
    self.assertEqual(tensor_shape.TensorShape([3]), dist.event_shape)
    self.assertEqual(tensor_shape.TensorShape([]), dist.batch_shape)
