# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
tensor_a = constant_op.constant([[42, 42], [42, 42]])
tensor_b = constant_op.constant([[24, 24], [24, 24]])
self._benchmark_add(tensor_a, tensor_b)
