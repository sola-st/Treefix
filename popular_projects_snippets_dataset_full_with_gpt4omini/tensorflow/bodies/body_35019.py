# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
for batch_shape in ([], [1], [2, 3, 4]):
    dist = make_bernoulli(batch_shape)
    self.assertAllEqual(batch_shape, dist.batch_shape.as_list())
    self.assertAllEqual(batch_shape, self.evaluate(dist.batch_shape_tensor()))
    self.assertAllEqual([], dist.event_shape.as_list())
    self.assertAllEqual([], self.evaluate(dist.event_shape_tensor()))
