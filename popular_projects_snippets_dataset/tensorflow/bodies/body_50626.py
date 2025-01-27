# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_test.py
with self.assertRaises(errors.InvalidArgumentError):
    invalid_sample_rate = [22000.0, 22000.0]
    self.evaluate(summary_lib.audio('', [[1.0]], invalid_sample_rate))
