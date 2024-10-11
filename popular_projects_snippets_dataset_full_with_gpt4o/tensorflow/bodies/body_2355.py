# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
"""Use Pearson's Chi-squared test to test for uniformity."""
self.check_dtype(dtype)
three_fry = random.Algorithm.THREEFRY.value
auto_select = random.Algorithm.AUTO_SELECT.value
is_tpu = xla_device().device_type == "TPU"
is_megacore = "megacore" in os.environ.get("TEST_TARGET", "").lower()
# TODO(b/244649364): Investigate why these combinations fail.
if ((alg, dtype, seed) in [(three_fry, dtypes.int64, 123),
                           (three_fry, dtypes.uint64, 123)] or
    is_tpu and
    (alg, dtype, seed) in [(auto_select, dtypes.int64, 123),
                           (auto_select, dtypes.uint64, 123)] or
    is_megacore and
    (alg, dtype, seed) in [(auto_select, dtypes.int32, 123),
                           (auto_select, dtypes.uint32, 123),
                           (auto_select, dtypes.int32, 12),
                           (auto_select, dtypes.uint32, 12)]):
    self.skipTest(
        "This (device, alg, dtype, seed) combination fails (b/244649364).")
with ops.device(xla_device_name()):
    n = 1000
    gen = random.Generator.from_seed(seed=seed, alg=alg)
    maxval = 1
    if dtype.is_integer:
        maxval = 100
    t = gen.uniform(shape=[n], maxval=maxval, dtype=dtype)
    x = t.numpy().astype(float)
    if maxval > 1:
        # Normalize y to range [0, 1).
        x = x / maxval
    # Tests that the values are distributed amongst 10 bins with equal
    # probability. 16.92 is the Chi^2 value for 9 degrees of freedom with
    # p=0.05. This test is probabilistic and would be flaky if the random
    # seed were not fixed.
    val = random_test_util.chi_squared(x, 10)
    self.assertLess(val, 16.92)
