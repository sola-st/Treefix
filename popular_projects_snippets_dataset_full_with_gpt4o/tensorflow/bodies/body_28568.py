# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
input_dataset = dataset_ops.Dataset.from_tensor_slices([])
concatenate_dataset = dataset_ops.Dataset.from_tensor_slices([2.0, 3.0])
concatenated = input_dataset.concatenate(concatenate_dataset)
self.assertAllEqual(
    self.evaluate(random_access.at(concatenated, index=0)), 2.0)
self.assertAllEqual(
    self.evaluate(random_access.at(concatenated, index=1)), 3.0)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(concatenated, index=2))
