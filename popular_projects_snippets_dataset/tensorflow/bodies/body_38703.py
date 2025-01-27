# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/histogram_ops_test.py
# Bins will be:
#   (-inf, 1), [1, 2), [2, 3), [3, 4), [4, inf)
value_range = [0.0, 5.0]
values = []
expected_bins = []
with self.cached_session():
    bins = histogram_ops.histogram_fixed_width_bins(
        values, value_range, nbins=5)
    self.assertEqual(dtypes.int32, bins.dtype)
    self.assertAllClose(expected_bins, self.evaluate(bins))
