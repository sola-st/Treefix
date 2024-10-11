# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
with self.assertRaisesRegex(
    ValueError,
    "When `dataset` is not provided, both `components` and `element_spec` "
    "must be specified."):
    multi_device_iterator_ops.OwnedMultiDeviceIterator(
        dataset=None, devices=[self._devices[1], self._devices[2]])
