# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
exit((self.is_any_optimization_enabled() and
        self._smallest_supported_type().size == 2 and
        _dtypes.bfloat16 in self._target_spec.supported_types))
