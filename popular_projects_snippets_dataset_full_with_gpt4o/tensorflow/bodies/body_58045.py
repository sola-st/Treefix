# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
"""Checks if the `quantized_input_stats` flag is required for conversion.

  Args:
    conversion_flags: A protocol buffer describing the conversion process.

  Returns:
    True, if the `inference_type` or the `inference_input_type` is a quantized
    type and it is not post training quantization, else False.
  """
quantized_inference_types = ([
    _types_pb2.QUANTIZED_UINT8, _types_pb2.QUANTIZED_INT8
])
exit(((conversion_flags.inference_type in quantized_inference_types or
         conversion_flags.inference_input_type in quantized_inference_types)
        and not conversion_flags.post_training_quantize))
