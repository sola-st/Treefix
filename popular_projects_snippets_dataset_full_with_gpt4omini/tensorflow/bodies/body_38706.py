# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/histogram_ops_test.py
value_range = [0.0, 5.0]
values = []
with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                            "must > 0"):
    with self.session():
        bins = histogram_ops.histogram_fixed_width_bins(
            values, value_range, nbins=-1)
        self.evaluate(bins)
