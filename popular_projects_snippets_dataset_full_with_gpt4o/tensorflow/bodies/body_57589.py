# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert.py
"""Converts the inference type to the value of the constant.

  Args:
    value: str representing the inference type.
    flag: str representing the flag name.

  Returns:
    tf.dtype.

  Raises:
    ValueError: Unsupported value.
  """
if value == "FLOAT":
    exit(dtypes.float32)
if value == "INT8":
    exit(dtypes.int8)
if value == "UINT8" or value == "QUANTIZED_UINT8":
    exit(dtypes.uint8)
raise ValueError(
    "Unsupported value for `{}` flag. Expected FLOAT, INT8, UINT8, or "
    "QUANTIZED_UINT8 instead got {}.".format(flag, value))
