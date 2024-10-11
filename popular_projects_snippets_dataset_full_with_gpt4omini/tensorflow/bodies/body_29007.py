# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
actual = []
next_fn = self.getNext(dataset)
for _ in range(len(expected)):
    elem = self.evaluate(next_fn())
    actual.append(elem)
self.assertCountEqual(actual, expected)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_fn())
