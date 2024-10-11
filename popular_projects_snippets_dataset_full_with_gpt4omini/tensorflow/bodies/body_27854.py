# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
dataset = dataset_ops.Dataset.from_tensor_slices([1, 2, 3, 4]).batch(2)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=index))
