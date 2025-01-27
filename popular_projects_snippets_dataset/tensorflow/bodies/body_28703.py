# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/memory_cleanup_test.py
if memory_profiler is None:
    self.skipTest("memory_profiler required to run this test")

dataset = dataset_ops.Dataset.range(10)
multi_device_iterator = multi_device_iterator_ops.MultiDeviceIterator(
    dataset, [self._devices[1], self._devices[2]])

def f():
    self.evaluate(multi_device_iterator.get_next())
    multi_device_iterator._eager_reset()

self.assertMemoryNotIncreasing(f, num_iters=50, max_increase_mb=250)
