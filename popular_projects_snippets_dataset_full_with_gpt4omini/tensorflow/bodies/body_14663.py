# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
self.assertAllEqual(len(a), len(b))
for x, y in zip(a, b):
    self.assertAllEqual(x, y)
