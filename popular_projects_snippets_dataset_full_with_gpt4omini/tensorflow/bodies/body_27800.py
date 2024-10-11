# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
dataset = dataset_ops.Dataset.range(1000)

mdi = multi_device_iterator_ops.OwnedMultiDeviceIterator(
    dataset, [self._devices[1], self._devices[2]],
    max_buffer_size=max_buffer_size,
    prefetch_buffer_size=prefetch_buffer_size)

for i, el in enumerate(mdi):
    self.assertEqual([i * 2, i * 2 + 1], [el[0].numpy(), el[1].numpy()])
