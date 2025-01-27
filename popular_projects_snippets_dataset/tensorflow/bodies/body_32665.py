# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
a_ = self.dtype([[1., .4, .5, 1.], [.4, .2, .25, 2.], [.5, .25, .35, 3.]])
a_ = np.stack([a_ + 0.5, a_], axis=0)  # Batch of matrices.
a = array_ops.placeholder_with_default(
    a_, shape=a_.shape if self.use_static_shape else None)
if self.use_default_rcond:
    rcond = None
else:
    # Smallest 2 components are forced to zero.
    rcond = self.dtype([0., 0.25])
expected_a_pinv_ = self.expected_pinv(a_, rcond)
a_pinv = linalg.pinv(a, rcond, validate_args=True)
a_pinv_ = self.evaluate(a_pinv)
self.assertAllClose(expected_a_pinv_, a_pinv_, atol=1e-5, rtol=1e-4)
if not self.use_static_shape:
    exit()
self.assertAllEqual(expected_a_pinv_.shape, a_pinv.shape)
