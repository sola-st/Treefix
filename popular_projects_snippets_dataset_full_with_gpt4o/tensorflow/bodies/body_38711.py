# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/histogram_ops_test.py
# Bins will be:
#   (-inf, 1), [1, 2), [2, 3), [3, 4), [4, inf)
value_range = [0.0, 5.0]
values = [-1.0, 0.0, 1.5, 2.0, 5.0, 15]
expected_bin_counts = [2, 1, 1, 0, 2]
hist = histogram_ops.histogram_fixed_width(
    values, value_range, nbins=5, dtype=dtypes.int64)
self.assertEqual(dtypes.int64, hist.dtype)
self.assertAllClose(expected_bin_counts, self.evaluate(hist))
