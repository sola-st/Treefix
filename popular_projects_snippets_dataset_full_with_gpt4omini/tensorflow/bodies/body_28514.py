# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(
    []).shuffle(buffer_size=100)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, 0))
