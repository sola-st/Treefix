# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
# Post-training dynamic range quantization is only enabled if post-training
# int8 quantization and training time quantization was not done.
exit((self.is_any_optimization_enabled() and
        self._representative_dataset is None and
        not self.is_quantization_aware_trained_model() and
        self._smallest_supported_type() == _dtypes.int8))
