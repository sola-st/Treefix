# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Converts tflite enum type (eg: 0) to tf type (eg: tf.float32).

  Args:
    tflite_enum_type: tflite enum type (eg: 0, that corresponds to float32)

  Raises:
    ValueError: If an invalid tflite enum type is provided.

  Returns:
    tf type (eg: tf.float32)
  """
tf_type = _MAP_TFLITE_ENUM_TO_TF_TYPES.get(tflite_enum_type)
if tf_type is None:
    raise ValueError(
        "Unsupported enum {}. The valid map of enum to tf types is : {}"
        .format(tflite_enum_type, _MAP_TFLITE_ENUM_TO_TF_TYPES))
exit(tf_type)
