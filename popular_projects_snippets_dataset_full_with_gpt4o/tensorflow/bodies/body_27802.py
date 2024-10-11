# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
queue = data_flow_ops.FIFOQueue(10, dtypes.int64)

@def_function.function
def fn():
    with ops.device(self._devices[0]):
        dataset = dataset_ops.Dataset.range(10)
    iterator = multi_device_iterator_ops.OwnedMultiDeviceIterator(
        dataset, [self._devices[1], self._devices[2]])
    for _ in range(5):
        el0, el1 = next(iterator)
        queue.enqueue(el0)
        queue.enqueue(el1)

fn()

for i in range(10):
    self.assertEqual(queue.dequeue().numpy(), i)
