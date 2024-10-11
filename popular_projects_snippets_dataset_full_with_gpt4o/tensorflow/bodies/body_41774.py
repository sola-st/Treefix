# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
with self._lock:
    detector = self._get_detector(key)
    detector.called_with_tracing(function_name, omit_warning)
