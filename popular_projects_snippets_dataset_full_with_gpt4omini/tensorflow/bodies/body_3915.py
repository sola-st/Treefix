# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container_test.py
container = self._prepare_function_captures()
capture = container.by_ref_captures["1"]
self.assertTrue(capture.is_by_ref)
