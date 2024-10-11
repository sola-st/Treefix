# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
input_dataset = dataset_ops.Dataset.from_tensor_slices([-1])
concatenate_dataset = dataset_ops.Dataset.from_tensor_slices([1, 2])
concatenated = input_dataset.concatenate(concatenate_dataset)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(concatenated, index=index))
