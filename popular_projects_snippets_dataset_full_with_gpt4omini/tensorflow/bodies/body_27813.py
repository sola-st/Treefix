# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
dataset = dataset_ops.Dataset.range(1000)
with self.assertRaisesRegex(
    ValueError,
    "When `dataset` is provided, `element_spec` and `components` must "
    "not be specified."):
    multi_device_iterator_ops.OwnedMultiDeviceIterator(
        dataset, devices=[self._devices[1], self._devices[2]],
        element_spec=dataset.element_spec)
