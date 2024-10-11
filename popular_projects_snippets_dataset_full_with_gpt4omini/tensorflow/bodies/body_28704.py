# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/memory_cleanup_test.py
multi_device_iterator = multi_device_iterator_ops.MultiDeviceIterator(
    dataset, [self._devices[1], self._devices[2]])
self.evaluate(multi_device_iterator.get_next())
del multi_device_iterator
