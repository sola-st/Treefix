# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/take_test.py
dataset = dataset_ops.Dataset.from_tensor_slices([]).take(5)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=index))
