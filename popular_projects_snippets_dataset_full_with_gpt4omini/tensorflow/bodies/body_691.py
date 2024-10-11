# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
rtol, atol = self.adjust_tolerance_for_tpu(dtype, rtol, atol)
if self.device not in ['XLA_GPU', 'XLA_CPU'] and dtype == np.float64:
    # TODO(b/165739664): Figure out why on TPU F64 Zeta sometimes returns
    # infs.
    self.skipTest(
        'Skipping test because some F64 operations are numerically '
        'unstable on TPU.')

x = np.random.uniform(low=100., high=200., size=[NUM_SAMPLES]).astype(dtype)
q = np.random.uniform(low=0.3, high=1., size=[NUM_SAMPLES]).astype(dtype)

expected_values = sps.zeta(x, q)
with self.session() as sess:
    with self.test_scope():
        y = _zeta(x, q)
    actual = sess.run(y)

self.assertAllClose(expected_values, actual, atol=atol, rtol=rtol)
