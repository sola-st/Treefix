# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
rtol, atol = self.adjust_tolerance_for_tpu(dtype, rtol, atol)
if self.device not in ['XLA_GPU', 'XLA_CPU'] and dtype == np.float64:
    self.skipTest(
        'Skipping test because some F64 operations are '
        'numerically unstable on TPU.'
    )

x = np.random.uniform(low=0.1, high=50., size=[NUM_SAMPLES]).astype(dtype)
expected_values = sps.digamma(x)
with self.session() as sess:
    with self.test_scope():
        y = _polygamma(dtype(0.), x)
    actual = sess.run(y)

self.assertAllClose(expected_values, actual, atol=atol, rtol=rtol)
