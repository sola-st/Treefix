# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
dataset = dataset_ops.Dataset.range(0)
multi_device_iterator = cls(
    dataset, devices=[self._devices[1], self._devices[2]])
with self.assertRaises(errors.OutOfRangeError):
    multi_device_iterator.get_next()
