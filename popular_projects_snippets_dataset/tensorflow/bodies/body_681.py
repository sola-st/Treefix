# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
# Test values near zero.
rtol, atol = self.adjust_tolerance_for_tpu(dtype, rtol, atol)
x = np.exp(np.random.uniform(
    low=low, high=high, size=[NUM_SAMPLES])).astype(dtype)
if is_negative:
    x = -x
expected_values = np.log1p(x)
with self.session() as sess:
    with self.test_scope():
        actual = _log1p(x)
    actual = sess.run(actual)
self.assertAllClose(expected_values, actual, atol=atol, rtol=rtol)
