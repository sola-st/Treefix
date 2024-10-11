# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
x = np.random.uniform(
    low=100., high=int(1e3), size=[NUM_SAMPLES]).astype(dtype)
q = np.random.uniform(
    low=1., high=int(1e1), size=[NUM_SAMPLES]).astype(dtype)

expected_values = sps.zeta(x, q)
with self.session() as sess:
    with self.test_scope():
        actual = sess.run(_zeta(x, q))
self.assertAllClose(expected_values, actual, atol=atol, rtol=rtol)
