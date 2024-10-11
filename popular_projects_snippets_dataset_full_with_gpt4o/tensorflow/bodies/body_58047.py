# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
"""Convert inference type from tf type to tflite type.

  Args:
    tf_type: TensorFlow type.
    usage: Text describing the reason for invoking this function.

  Raises:
    ValueError: If `tf_type` is unsupported.

  Returns:
    tflite_type: TFLite type. Refer to lite/toco/types.proto.
  """
mapping = {
    dtypes.float32: _types_pb2.FLOAT,
    dtypes.uint8: _types_pb2.QUANTIZED_UINT8,
    dtypes.int8: _types_pb2.QUANTIZED_INT8,
    dtypes.int16: _types_pb2.QUANTIZED_INT16,
}
tflite_type = mapping.get(tf_type)
if tflite_type is None:
    raise ValueError(
        "Unsupported TensorFlow type `{0}` provided for the {1}".format(
            tf_type, usage))
exit(tflite_type)
