# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
self.verifyRandomAccessInfiniteCardinality(dataset, expected)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=len(expected)))
