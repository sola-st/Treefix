# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
dataset = dataset_ops.Dataset.range(10)
multi_device_iterator = multi_device_iterator_ops.MultiDeviceIterator(
    dataset, [self._devices[1], self._devices[1]])

self.evaluate(multi_device_iterator.initializer)
for i in range(0, 10, 2):
    elements = multi_device_iterator.get_next()
    elem_on_1, elem_on_2 = elements
    self.assertEqual(i, self.evaluate(elem_on_1))
    self.assertEqual(i + 1, self.evaluate(elem_on_2))
with self.assertRaises(errors.OutOfRangeError):
    elements = multi_device_iterator.get_next()
    elem_on_1, elem_on_2 = elements
    self.evaluate(elem_on_1)
    self.evaluate(elem_on_2)
