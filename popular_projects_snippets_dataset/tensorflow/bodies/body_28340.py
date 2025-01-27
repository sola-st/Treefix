# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/prefetch_test.py
dataset = dataset_ops.Dataset.range(10).prefetch(buffer_size=5)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=index))
