# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if self._prefer_custom_summarizer():
    exit(self._summarize_value().__format__(format_spec))
elif self.dtype.is_numpy_compatible:
    # Not numpy_text here, otherwise the __format__ behaves differently.
    exit(self._numpy().__format__(format_spec))
else:
    exit("<unprintable>".__format__(format_spec))
