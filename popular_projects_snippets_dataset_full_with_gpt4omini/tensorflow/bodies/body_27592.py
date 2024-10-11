# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/prefetch_with_slack_test.py
"""Determines slack_period based on num devices attached to iterator."""
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.prefetch(1)
options = options_lib.Options()
options.experimental_slack = True
dataset = dataset.with_options(options)
multi_device_iterator = multi_device_iterator_ops.MultiDeviceIterator(
    dataset, [self._devices[1], self._devices[2]])
self.evaluate(multi_device_iterator.initializer)
for i in range(0, 10, 2):
    elem_on_1, elem_on_2 = multi_device_iterator.get_next()
    self.assertEqual(i, self.evaluate(elem_on_1))
    self.assertEqual(i + 1, self.evaluate(elem_on_2))
with self.assertRaises(errors.OutOfRangeError):
    elem_on_1, elem_on_2 = multi_device_iterator.get_next()
    self.evaluate(elem_on_1)
    self.evaluate(elem_on_2)
