# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
if self.device == 'TPU':
    # TODO(b/154908275): Remove this once fixed for large a, x.
    self.skipTest('Skipping test since numerically unstable on TPU.')
# Test values near zero.
x = np.random.uniform(
    low=100., high=int(1e4), size=[NUM_SAMPLES]).astype(dtype)
a = np.random.uniform(
    low=100., high=int(1e4), size=[NUM_SAMPLES]).astype(dtype)

expected_values = sps.gammainc(a, x)
with self.session() as sess:
    with self.test_scope():
        actual = sess.run(_igamma(a, x))
self.assertAllClose(expected_values, actual, atol=atol, rtol=rtol)
