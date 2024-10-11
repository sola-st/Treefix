# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
rtol, atol = self.adjust_tolerance_for_tpu(dtype, rtol, atol)
n = np.random.randint(low=5, high=10, size=[NUM_SAMPLES]).astype(dtype)
x = np.random.uniform(low=1., high=1e1, size=[NUM_SAMPLES]).astype(dtype)

expected_values = sps.polygamma(n, x)
with self.session() as sess:
    with self.test_scope():
        actual = sess.run(_polygamma(n, x))
self.assertAllClose(expected_values, actual, atol=atol, rtol=rtol)
