# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
dataset = dataset_ops.Dataset.from_tensors([])
self.assertAllEqual(self.evaluate(random_access.at(dataset, 0)), [])
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, 1))
