# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/skip_test.py
dataset = dataset_ops.Dataset.range(10).skip(8)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=index))
