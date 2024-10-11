# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/flatbuffer_utils.py
"""Writes the tflite model, a python object, into the output file.

  Args:
    model_object: A tflite model as a python object
    output_tflite_file: Full path name to the output tflite file.

  Raises:
    IOError: If output_tflite_file path is invalid or cannot be opened.
  """
model_bytearray = convert_object_to_bytearray(model_object)
with gfile.GFile(output_tflite_file, 'wb') as output_file_handle:
    output_file_handle.write(model_bytearray)
