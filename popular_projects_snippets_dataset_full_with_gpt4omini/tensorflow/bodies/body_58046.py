# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
"""Convert tensor type from tf type to tflite type.

  Args:
    tf_type: TensorFlow type.
    usage: Text describing the reason for invoking this function.

  Raises:
    ValueError: If `tf_type` is unsupported.

  Returns:
    tflite_type: TFLite type. Refer to lite/toco/types.proto.
  """
mapping = {
    dtypes.float16: _types_pb2.FLOAT16,
    dtypes.float32: _types_pb2.FLOAT,
    dtypes.float64: _types_pb2.FLOAT64,
    dtypes.int8: _types_pb2.INT8,
    dtypes.int16: _types_pb2.INT16,
    dtypes.uint16: _types_pb2.UINT16,
    dtypes.int32: _types_pb2.INT32,
    dtypes.int64: _types_pb2.INT64,
    dtypes.uint8: _types_pb2.UINT8,
    dtypes.uint32: _types_pb2.UINT32,
    dtypes.uint64: _types_pb2.UINT64,
    dtypes.string: _types_pb2.STRING,
    dtypes.bool: _types_pb2.BOOL,
    dtypes.complex64: _types_pb2.COMPLEX64,
    dtypes.complex128: _types_pb2.COMPLEX128,
}
tflite_type = mapping.get(tf_type)
if tflite_type is None:
    raise ValueError(
        "Unsupported TensorFlow type `{0}` provided for the {1}".format(
            tf_type, usage))
exit(tflite_type)
