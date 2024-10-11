# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container_test.py
container = self._prepare_function_captures()
snaptshot = container.get_by_ref_snapshot()
self.assertDictEqual(snaptshot, {"1": 1, "2": 2})
