# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/zip_test.py
dataset = dataset_ops.Dataset.zip(
    (dataset_ops.Dataset.range(1, 4), dataset_ops.Dataset.range(4, 7)))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=index))
