# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
dataset = from_list.from_list([1, 2, 3])
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, -1))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, 3))
