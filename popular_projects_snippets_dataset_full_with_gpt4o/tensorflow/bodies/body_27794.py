# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
dataset = dataset_ops.Dataset.range(10)
multi_device_iterator = multi_device_iterator_ops.MultiDeviceIterator(
    dataset, [self._devices[1], self._devices[2]])

self.evaluate(multi_device_iterator.initializer)
for i in range(0, 10, 2):
    elem_on_1, elem_on_2 = multi_device_iterator.get_next_as_optional()
    has_elem_1, get_elem_1 = self.evaluate(
        [elem_on_1.has_value(), elem_on_1.get_value()])
    has_elem_2, get_elem_2 = self.evaluate(
        [elem_on_2.has_value(), elem_on_2.get_value()])
    self.assertTrue(has_elem_1)
    self.assertEqual(i, get_elem_1)
    self.assertTrue(has_elem_2)
    self.assertEqual(i + 1, get_elem_2)
elem_on_1, elem_on_2 = multi_device_iterator.get_next_as_optional()
has_elem_1 = elem_on_1.has_value()
has_elem_2 = elem_on_2.has_value()
self.assertFalse(self.evaluate(has_elem_1))
self.assertFalse(self.evaluate(has_elem_2))
with self.assertRaises(errors.InvalidArgumentError):
    elem_1 = elem_on_1.get_value()
    self.evaluate(elem_1)
with self.assertRaises(errors.InvalidArgumentError):
    elem_2 = elem_on_2.get_value()
    self.evaluate(elem_2)
