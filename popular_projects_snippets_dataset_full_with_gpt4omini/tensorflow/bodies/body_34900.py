# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bijector_test.py
broken_bijector = self.broken_bijector_cls(inverse_missing=True)
x = constant_op.constant(1.1)

# Call forward and forward_log_det_jacobian one-by-one (not together).
y = broken_bijector.forward(x)
_ = broken_bijector.forward_log_det_jacobian(x, event_ndims=0)

# Now, everything should be cached if the argument is y.
broken_bijector.inverse(y)
broken_bijector.inverse_log_det_jacobian(y, event_ndims=0)

# Different event_ndims should not be cached.
with self.assertRaises(IntentionallyMissingError):
    broken_bijector.inverse_log_det_jacobian(y, event_ndims=1)
