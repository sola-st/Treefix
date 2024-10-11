# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/histogram_ops_test.py
values = [-1.0, 0.0, 1.5, 2.0, 5.0, 15]
with self.assertRaisesRegex(
    (errors.InvalidArgumentError, ValueError),
    "Shape must be rank 1 but is rank 0|should be a vector"):
    self.evaluate(histogram_ops.histogram_fixed_width(values, 1.0))
with self.assertRaisesRegex(
    (errors.InvalidArgumentError, ValueError),
    "Dimension must be 2 but is 3|should be a vector of 2 elements"):
    self.evaluate(
        histogram_ops.histogram_fixed_width(values, [1.0, 2.0, 3.0]))
