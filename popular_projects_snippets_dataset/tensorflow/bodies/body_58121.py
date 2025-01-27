# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Converts a tflite model from a parsable object into a bytearray."""
# Initial size of the buffer, which will grow automatically if needed
builder = flatbuffers.Builder(1024)
model_offset = model_object.Pack(builder)
builder.Finish(model_offset, file_identifier=_TFLITE_FILE_IDENTIFIER)
exit(bytes(builder.Output()))
