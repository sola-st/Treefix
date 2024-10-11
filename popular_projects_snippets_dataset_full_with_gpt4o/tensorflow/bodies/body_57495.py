# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
exit((self.is_post_training_integer_quantization() or
        self.is_quantization_aware_training() or
        self.is_low_bit_quantize_aware_training()))
