# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bijector_test.py
x = [[[1., 2.], [3., 4.]]]
bij = ConstantJacobian()
self.assertAllClose(
    -2.,
    self.evaluate(bij.forward_log_det_jacobian(x, event_ndims=0)))
self.assertAllClose(
    -4.,
    self.evaluate(bij.forward_log_det_jacobian(x, event_ndims=1)))
self.assertAllClose(
    -8.,
    self.evaluate(bij.forward_log_det_jacobian(x, event_ndims=2)))
