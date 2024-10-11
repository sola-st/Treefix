# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
dataset = dataset_ops.Dataset.range(9)
multi_device_iterator = multi_device_iterator_ops.MultiDeviceIterator(
    dataset, [self._devices[1], self._devices[2]])

self.evaluate(multi_device_iterator.initializer)
for i in range(0, 8, 2):
    elem_on_1, elem_on_2 = multi_device_iterator.get_next()
    self.assertEqual(i, self.evaluate(elem_on_1))
    self.assertEqual(i + 1, self.evaluate(elem_on_2))
elem_on_1 = multi_device_iterator.get_next(self._devices[1])
self.assertEqual(8, self.evaluate(elem_on_1))
with self.assertRaises(errors.OutOfRangeError):
    elem_on_1, elem_on_2 = multi_device_iterator.get_next()
    self.evaluate(elem_on_1)
    self.evaluate(elem_on_2)
