# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with self.cached_session():
    x = constant(1.0)
    y = x * 2.0
    z = y + y + y + y + y + y + y + y + y + y
    grads = gradients.gradients(
        z, [x, y], aggregation_method=gradients.AggregationMethod.ADD_N)
    self.assertTrue(all(x is not None for x in grads))
    self.assertEqual(20.0, grads[0].eval())
    self.assertEqual(10.0, grads[1].eval())
