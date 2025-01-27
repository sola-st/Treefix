# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/memory_cleanup_test.py
if memory_profiler is None:
    self.skipTest("memory_profiler required to run this test")

dataset = dataset_ops.Dataset.range(10)

def f():
    multi_device_iterator = multi_device_iterator_ops.MultiDeviceIterator(
        dataset, [self._devices[1], self._devices[2]])
    self.evaluate(multi_device_iterator.get_next())
    del multi_device_iterator

# TODO(b/123316347): Reduce threshold once bug is fixed.
self.assertMemoryNotIncreasing(f, num_iters=50, max_increase_mb=250)
