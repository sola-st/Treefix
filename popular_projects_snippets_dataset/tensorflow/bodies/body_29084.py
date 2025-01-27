# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/range_test.py
dataset = dataset_ops.Dataset.range(2)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=index))
