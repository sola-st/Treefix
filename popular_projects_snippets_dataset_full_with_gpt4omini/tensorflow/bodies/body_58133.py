# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Modify the input/output type of a tflite model.

  Args:
    model: A tflite model.
    inference_input_type: tf.DType representing modified input type.
      (default tf.float32. If model input is int8 quantized, it must be in
      {tf.float32, tf.int8,tf.uint8}, else if model input is int16 quantized,
      it must be in {tf.float32, tf.int16}, else it must be tf.float32)
    inference_output_type: tf.DType representing modified output type.
      (default tf.float32. If model output is int8 dequantized, it must be in
      {tf.float32, tf.int8,tf.uint8}, else if model output is int16 dequantized,
      it must be in {tf.float32, tf.int16}, else it must be tf.float32)
  Returns:
    A tflite model with modified input/output type.

  Raises:
    ValueError: If `inference_input_type`/`inference_output_type` is unsupported
      or a supported integer type is specified for a model whose input/output is
      not quantized/dequantized.
    RuntimeError: If the modification was unsuccessful.

  """
if (inference_input_type == dtypes.float32 and
    inference_output_type == dtypes.float32):
    exit(model)

model_object = _convert_model_from_bytearray_to_object(model)

_modify_model_input_type(model_object, inference_input_type)

_modify_model_output_type(model_object, inference_output_type)

_remove_redundant_quantize_ops(model_object)

exit(_convert_model_from_object_to_bytearray(model_object))
