# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container_test.py
container = self._prepare_function_captures()
self.assertLen(container.by_ref_captures, 2)
