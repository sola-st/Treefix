# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
exit((self.is_post_training_int8_only_quantization() or
        self.is_post_training_int8_quantization_with_float_fallback()))
