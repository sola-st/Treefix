# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Validate inference_input_type and inference_output_type flags."""
default_types = [_dtypes.float32]
# We support integer input/output for integer quantized models only.
if quant_mode.is_integer_quantization():
    if quant_mode.is_post_training_int16x8_quantization():
        all_types = default_types + [_dtypes.int16]
    else:
        all_types = default_types + [_dtypes.int8, _dtypes.uint8]
    if (self.inference_input_type not in all_types or
        self.inference_output_type not in all_types):
        all_types_names = ["tf." + t.name for t in all_types]
        raise ValueError("The inference_input_type and inference_output_type "
                         "must be in {}.".format(all_types_names))
elif (self.inference_input_type not in default_types or
      self.inference_output_type not in default_types):
    raise ValueError("The inference_input_type and inference_output_type "
                     "must be tf.float32.")
