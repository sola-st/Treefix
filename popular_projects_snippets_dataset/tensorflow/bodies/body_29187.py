# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/take_test.py
dataset = dataset_ops.Dataset.range(10).take(3)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=index))
