# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bijector_test.py
x = [[[1., 2.], [3., 4.]]]
bij = ExpOnlyJacobian(forward_min_event_ndims=1)
with self.assertRaisesRegex(ValueError, "must be larger than"):
    bij.forward_log_det_jacobian(x, event_ndims=0)
