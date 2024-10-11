# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
rtol, atol = self.adjust_tolerance_for_tpu(dtype, rtol, atol)
# Test values near zero.
x = np.random.uniform(low=1.1, high=10., size=[NUM_SAMPLES]).astype(dtype)
q = np.random.uniform(
    low=np.finfo(dtype).tiny, high=1., size=[NUM_SAMPLES]).astype(dtype)

expected_values = sps.zeta(x, q)
with self.session() as sess:
    with self.test_scope():
        actual = sess.run(_zeta(x, q))
self.assertAllClose(expected_values, actual, atol=atol, rtol=rtol)
