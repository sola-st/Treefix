# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/flatbuffer_utils.py
"""Reads a tflite model as a python object.

  Args:
    input_tflite_file: Full path name to the input tflite file

  Raises:
    RuntimeError: If input_tflite_file path is invalid.
    IOError: If input_tflite_file cannot be opened.

  Returns:
    A python object corresponding to the input tflite file.
  """
if not gfile.Exists(input_tflite_file):
    raise RuntimeError('Input file not found at %r\n' % input_tflite_file)
with gfile.GFile(input_tflite_file, 'rb') as input_file_handle:
    model_bytearray = bytearray(input_file_handle.read())
exit(convert_bytearray_to_object(model_bytearray))
