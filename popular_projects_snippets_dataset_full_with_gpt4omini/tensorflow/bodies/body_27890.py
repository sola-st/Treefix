# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
dataset = dataset_ops.Dataset.from_tensors([1, 2, 3])
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, -1))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, 1))
