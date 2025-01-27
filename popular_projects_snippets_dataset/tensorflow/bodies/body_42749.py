# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = constant_op.constant([], dtype=np.float32)
self.assertAllEqual(np.array(memoryview(t)), np.array([]))
