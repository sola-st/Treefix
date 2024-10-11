# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
x = np.array([[3., 4., 5.]], np.float32)
y = self.backend.buffer_from_pyval(x)
self.assertIsNone(y.aval)
self.assertIsNone(y._device)
