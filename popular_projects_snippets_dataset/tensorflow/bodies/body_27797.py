# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
dataset1 = dataset_ops.Dataset.range(1000)
dataset2 = dataset_ops.Dataset.range(1000)
dataset = dataset_ops.Dataset.zip((dataset1, dataset2))

for _ in range(5):
    multi_device_iterator = multi_device_iterator_ops.MultiDeviceIterator(
        dataset, [self._devices[1], self._devices[2]], prefetch_buffer_size=4)
    self.evaluate(multi_device_iterator.initializer)
    elem_on_1, elem_on_2 = multi_device_iterator.get_next()
    self.assertEqual([(0, 0), (1, 1)], self.evaluate([elem_on_1, elem_on_2]))
