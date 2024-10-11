# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
with ops.device("/device:GPU:0"):
    t = constant_op.constant([0.0])
self.assertAllEqual(
    np.array(memoryview(t)), np.array([0.0], dtype=np.float32))
