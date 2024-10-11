# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
"""Use Pearson's Chi-squared test to test for uniformity."""
philox = stateless.Algorithm.PHILOX
auto_select = stateless.Algorithm.AUTO_SELECT
device = xla_device()
if 'CPU' in device.device_type:
    device_type = 'CPU'
elif 'GPU' in device.device_type:
    device_type = 'GPU'
elif device.device_type == 'TPU':
    device_type = 'TPU'
else:
    device_type = None
bad_combos1 = [
    (dtypes.int32, [123, 456]),
    (dtypes.int64, [123, 456]),
    (dtypes.float16, [565656, 121212]),
    (dtypes.bfloat16, [1, 2]),
]
bad_combos2 = [
    (dtypes.int32, [1, 2]),
    (dtypes.int32, [12, 23]),
]
# TODO(b/244649364): Investigate why these combinations fail.
if (device_type in ('CPU', 'GPU') and alg in (philox, auto_select) and
    (dtype, seed) in bad_combos1 or device_type == 'TPU' and
    (alg == philox and
     (dtype, seed) in bad_combos1 or alg == auto_select and
     (dtype, seed) in bad_combos2)):
    self.skipTest(
        'This (device, alg, dtype, seed) combination fails (b/244649364).')
with self.session() as sess, self.test_scope():
    seed_t = array_ops.placeholder(dtypes.int32, shape=[2])
    n = 1000
    maxval = 1
    if dtype.is_integer:
        maxval = 100
    x = stateless.stateless_random_uniform(
        shape=[n], seed=seed_t, maxval=maxval, dtype=dtype, alg=alg)
    y = sess.run(x, {seed_t: seed})
    # Convert y to float and normalize its value to range [0, 1) when
    # maxval != 1.
    y = y.astype(float) / maxval
    # Tests that the values are distributed amongst 10 bins with equal
    # probability. 16.92 is the Chi^2 value for 9 degrees of freedom with
    # p=0.05. This test is probabilistic and would be flaky if the random
    # seed were not fixed.
    self.assertLess(random_test_util.chi_squared(y, 10), 16.92)
