# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
dataset = dataset_ops.Dataset.range(1000)

for _ in range(5):
    multi_device_iterator = (
        multi_device_iterator_ops.OwnedMultiDeviceIterator(
            dataset, [self._devices[1], self._devices[2]]))
    for i, el in enumerate(multi_device_iterator):
        self.assertEqual([i * 2, i * 2 + 1], [el[0].numpy(), el[1].numpy()])
