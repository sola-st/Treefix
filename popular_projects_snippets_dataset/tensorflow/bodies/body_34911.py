# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bijector_test.py
x = [[[1., 2.], [3., 4.]]]
bij = ExpOnlyJacobian()
self.assertAllClose(
    -np.log(x),
    self.evaluate(bij.inverse_log_det_jacobian(x, event_ndims=0)))
self.assertAllClose(
    np.sum(-np.log(x), axis=-1),
    self.evaluate(bij.inverse_log_det_jacobian(x, event_ndims=1)))
self.assertAllClose(
    np.sum(-np.log(x), axis=(-1, -2)),
    self.evaluate(bij.inverse_log_det_jacobian(x, event_ndims=2)))
