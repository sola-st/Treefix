# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/histogram_ops_test.py
# Bins will be:
#   (-inf, 1), [1, 2), [2, 3), [3, 4), [4, inf)
value_range = [0.0, 5.0]
values = []
expected_bin_counts = [0, 0, 0, 0, 0]
hist = histogram_ops.histogram_fixed_width(values, value_range, nbins=5)
self.assertEqual(dtypes.int32, hist.dtype)
self.assertAllClose(expected_bin_counts, self.evaluate(hist))
