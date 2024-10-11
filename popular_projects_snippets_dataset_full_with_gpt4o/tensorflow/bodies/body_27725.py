# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/skip_test.py
dataset = dataset_ops.Dataset.range(4).skip(skip)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=0))
