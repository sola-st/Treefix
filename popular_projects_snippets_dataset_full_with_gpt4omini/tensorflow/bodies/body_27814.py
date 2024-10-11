# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
dataset = dataset_ops.Dataset.range(1000)
with self.assertRaisesRegex(
    RuntimeError,
    "OwnedMultiDeviceIterator is only supported inside of tf.function or "
    "when eager execution is enabled."):
    multi_device_iterator_ops.OwnedMultiDeviceIterator(
        dataset, devices=[self._devices[1], self._devices[2]])
