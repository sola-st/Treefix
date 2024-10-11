# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
input_dataset = dataset_ops.Dataset.from_tensor_slices([1.0])
concatenate_dataset = dataset_ops.Dataset.from_tensor_slices([])
concatenated = input_dataset.concatenate(concatenate_dataset)
self.assertAllEqual(
    self.evaluate(random_access.at(concatenated, index=0)), 1.0)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(concatenated, index=1))
