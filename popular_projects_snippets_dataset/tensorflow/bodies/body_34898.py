# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bijector_test.py
bij = BrokenBijector(validate_args=True)
event_ndims = array_ops.placeholder(dtype=np.int32, shape=None)
with self.cached_session():
    with self.assertRaisesOpError("Expected scalar"):
        bij.forward_log_det_jacobian(1., event_ndims=event_ndims).eval({
            event_ndims: (1, 2)})
    with self.assertRaisesOpError("Expected scalar"):
        bij.inverse_log_det_jacobian(1., event_ndims=event_ndims).eval({
            event_ndims: (1, 2)})
