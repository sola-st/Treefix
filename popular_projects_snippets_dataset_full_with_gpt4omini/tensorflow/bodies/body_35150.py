# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/identity_bijector_test.py
bijector = identity_bijector.Identity(validate_args=True)
self.assertEqual("identity", bijector.name)
x = [[[0.], [1.]]]
self.assertAllEqual(x, self.evaluate(bijector.forward(x)))
self.assertAllEqual(x, self.evaluate(bijector.inverse(x)))
self.assertAllEqual(
    0.,
    self.evaluate(
        bijector.inverse_log_det_jacobian(x, event_ndims=3)))
self.assertAllEqual(
    0.,
    self.evaluate(
        bijector.forward_log_det_jacobian(x, event_ndims=3)))
