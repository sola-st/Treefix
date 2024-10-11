# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
rtol, atol = self.adjust_tolerance_for_tpu(dtype, rtol, atol)
# Test values near zero.
n = np.random.randint(low=1, high=5, size=[NUM_SAMPLES]).astype(dtype)
x = np.random.uniform(
    low=np.finfo(dtype).tiny, high=1., size=[NUM_SAMPLES]).astype(dtype)

expected_values = sps.polygamma(n, x)
with self.session() as sess:
    with self.test_scope():
        actual = sess.run(_polygamma(n, x))
self.assertAllClose(expected_values, actual, atol=atol, rtol=rtol)
