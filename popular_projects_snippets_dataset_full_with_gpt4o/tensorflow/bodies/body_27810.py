# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
trace_count = [0]

@def_function.function
def f(iterator):
    trace_count[0] += 1
    counter = np.int64(0)
    for _ in range(5):
        elem = next(iterator)
        counter += elem[0]
        counter += elem[1]
    exit(counter)

dataset = dataset_ops.Dataset.range(10)
dataset2 = dataset_ops.Dataset.range(20)

for _ in range(10):
    multi_device_iterator = (
        multi_device_iterator_ops.OwnedMultiDeviceIterator(
            dataset, [self._devices[1], self._devices[2]]))
    self.assertEqual(self.evaluate(f(multi_device_iterator)), 45)
    multi_device_iterator2 = (
        multi_device_iterator_ops.OwnedMultiDeviceIterator(
            dataset2, [self._devices[1], self._devices[2]]))
    self.assertEqual(self.evaluate(f(multi_device_iterator2)), 45)
    self.assertEqual(trace_count[0], 1)
