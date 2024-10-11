# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
with self.assertRaises(errors.CancelledError):
    self.evaluate(op)
