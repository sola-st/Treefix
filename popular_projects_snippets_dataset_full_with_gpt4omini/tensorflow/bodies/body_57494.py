# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
exit((self.is_any_optimization_enabled() and
        self.is_quantization_aware_trained_model() and
        not self.is_low_bit_quantize_aware_training()))
