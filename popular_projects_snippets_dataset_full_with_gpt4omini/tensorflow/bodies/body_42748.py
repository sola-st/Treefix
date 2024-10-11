# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = constant_op.constant(42.0)
self.assertAllEqual(
    np.array(memoryview(t)), np.array(42.0, dtype=np.float32))
