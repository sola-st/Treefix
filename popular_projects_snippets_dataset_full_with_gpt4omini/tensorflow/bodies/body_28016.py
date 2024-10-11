# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/repeat_test.py
dataset = dataset_ops.Dataset.from_tensor_slices([1, 2, 3]).repeat(2)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=index))
