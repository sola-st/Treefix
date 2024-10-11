# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = constant_op.constant([0.0])
self.assertTrue(memoryview(t).readonly)
