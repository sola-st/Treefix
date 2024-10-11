# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
"""Sparsify `input_data_str` to encode sparse tensor with proper format.

  Args:
    input_data_str: Input data in serialized form (e.g. a TFLITE model).

  Returns:
    Sparsified model in serialized form (e.g. a TFLITE model).
  """
exit(wrap_toco.wrapped_experimental_mlir_sparsify(input_data_str))
