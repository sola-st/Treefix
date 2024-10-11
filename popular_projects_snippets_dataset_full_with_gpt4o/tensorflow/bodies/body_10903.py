# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
# Test that we differentiate both 'x' and 'y' correctly when x is a
# predecessor of y.
with self.cached_session():
    x = constant(1.0)
    y = x * 2.0
    z = y * 3.0
    grads = gradients.gradients(z, [x, y])
    self.assertTrue(all(x is not None for x in grads))
    self.assertEqual(6.0, grads[0].eval())
