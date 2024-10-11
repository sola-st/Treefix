# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.apply(testing.assert_next(["MemoryCacheImpl"]))
dataset = dataset.skip(0)  # this should be optimized away
dataset = dataset.cache()

options = options_lib.Options()
options.experimental_optimization.noop_elimination = True
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
