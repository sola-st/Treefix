# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
exit((self.is_any_optimization_enabled() and
        self._representative_dataset is not None and
        not self._is_int16x8_target_required() and
        not self.is_allow_float() and
        self._is_int8_target_required()))
