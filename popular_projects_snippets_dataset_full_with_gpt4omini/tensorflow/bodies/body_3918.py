# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container_test.py
container = self._prepare_function_captures()
lam = lambda: 12345
res = container._create_capture_placeholder(lam)
self.assertEqual(res, 12345)
