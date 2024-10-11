# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/python/modify_model_interface_lib.py
"""Converts a tflite type to it's integer representation.

  Args:
    dtype: tf.DType representing the inference type.
    flag: str representing the flag name.

  Returns:
     integer, a tflite TensorType enum value.

  Raises:
    ValueError: Unsupported tflite type.
  """
# Validate if dtype is supported in tflite and is a valid interface type.
if dtype not in mmi_constants.TFLITE_TYPES:
    raise ValueError(
        "Unsupported value '{0}' for {1}. Only {2} are supported.".format(
            dtype, flag, mmi_constants.TFLITE_TYPES))

dtype_str = mmi_constants.TFLITE_TO_STR_TYPES[dtype]
dtype_int = schema_fb.TensorType.__dict__[dtype_str]

exit(dtype_int)
