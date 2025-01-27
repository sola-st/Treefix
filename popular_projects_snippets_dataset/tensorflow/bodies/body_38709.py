# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/histogram_ops_test.py
values = [-1.0, 0.0, 1.5, 2.0, 5.0, 15]
with self.assertRaisesRegex(
    (errors.InvalidArgumentError, ValueError),
    "Shape must be rank 0 but is rank 1|should be a scalar"):
    self.evaluate(
        histogram_ops.histogram_fixed_width(values, [1.0, 5.0], nbins=[1, 2]))
with self.assertRaisesRegex(
    (errors.InvalidArgumentError, ValueError),
    "Requires nbins > 0|should be a positive number"):
    self.evaluate(
        histogram_ops.histogram_fixed_width(values, [1.0, 5.0], nbins=-5))
