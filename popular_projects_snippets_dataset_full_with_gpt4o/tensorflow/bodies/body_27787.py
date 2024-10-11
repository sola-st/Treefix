# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
dataset = dataset_ops.Dataset.range(10)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Length for attr 'devices' of 0 must be at least minimum 1"):
    cls(dataset, devices=[])
