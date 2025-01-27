# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
input_dataset = dataset_ops.Dataset.from_tensor_slices([0, 1, 2])
concatenate_dataset = dataset_ops.Dataset.from_tensor_slices([3, 4])
concatenated = input_dataset.concatenate(concatenate_dataset)
for i in range(5):
    self.assertAllEqual(random_access.at(concatenated, index=i), i)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(concatenated, index=5))
