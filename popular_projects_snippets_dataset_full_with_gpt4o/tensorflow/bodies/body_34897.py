# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bijector_test.py
bij = BrokenBijector()
with self.assertRaisesRegex(ValueError, "Expected scalar"):
    bij.forward_log_det_jacobian(1., event_ndims=(1, 2))
with self.assertRaisesRegex(ValueError, "Expected scalar"):
    bij.inverse_log_det_jacobian(1., event_ndims=(1, 2))
