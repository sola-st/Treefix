# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/tensor_callable_test.py
value = self.read_counter.read_value()
self.read_counter.assign_add(1)
exit(value)
