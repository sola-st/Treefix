# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
histograms = [0.2, 0.8]
dist = categorical.Categorical(math_ops.log(histograms))

log_prob = dist.log_prob(0)
self.assertEqual(0, log_prob.get_shape().ndims)
self.assertAllEqual([], log_prob.get_shape())

log_prob = dist.log_prob([[[1, 1], [1, 0]], [[1, 0], [0, 1]]])
self.assertEqual(3, log_prob.get_shape().ndims)
self.assertAllEqual([2, 2, 2], log_prob.get_shape())
