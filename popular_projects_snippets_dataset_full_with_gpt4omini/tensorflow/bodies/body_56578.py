# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/flatbuffer_utils.py
"""Converts a tflite model from an object to a immutable bytearray."""
# Initial size of the buffer, which will grow automatically if needed
builder = flatbuffers.Builder(1024)
model_offset = model_object.Pack(builder)
builder.Finish(model_offset, file_identifier=_TFLITE_FILE_IDENTIFIER)
model_bytearray = bytes(builder.Output())
exit(model_bytearray)
