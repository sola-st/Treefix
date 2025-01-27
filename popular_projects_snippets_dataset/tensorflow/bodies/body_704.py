# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
self.maybe_skip_test(dtype)
rtol, atol = self.adjust_tolerance_for_tpu(dtype, rtol, atol)
# Test values near zero.
x = np.random.uniform(low=100., high=200., size=[NUM_SAMPLES]).astype(dtype)
a = np.random.uniform(low=0.3, high=1., size=[NUM_SAMPLES]).astype(dtype)

expected_values = sps.gammainc(a, x)
with self.session() as sess:
    with self.test_scope():
        y = _igamma(a, x)
    actual = sess.run(y)
self.assertAllClose(expected_values, actual, atol=atol, rtol=rtol)
