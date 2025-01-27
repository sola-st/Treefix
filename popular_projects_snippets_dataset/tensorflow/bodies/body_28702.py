# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/memory_cleanup_test.py
self.evaluate(multi_device_iterator.get_next())
multi_device_iterator._eager_reset()
