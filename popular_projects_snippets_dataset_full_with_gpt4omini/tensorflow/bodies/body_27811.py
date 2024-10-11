# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
dataset = dataset_ops.Dataset.range(1000)
with self.assertRaisesRegex(ValueError, "`devices` must be provided."):
    multi_device_iterator_ops.OwnedMultiDeviceIterator(dataset)
