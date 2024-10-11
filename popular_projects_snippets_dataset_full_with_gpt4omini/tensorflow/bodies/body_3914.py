# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container_test.py
container = self._prepare_function_captures()
idf = len(container.by_ref_captures)
container.capture_by_ref(lambda: 12345)
capture = container.by_ref_captures[idf]
lam = capture.external
self.assertEqual(lam(), 12345)
