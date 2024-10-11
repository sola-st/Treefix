# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/flatbuffer_utils.py
"""Converts a tflite model from a bytearray to an object for parsing."""
model_object = schema_fb.Model.GetRootAsModel(model_bytearray, 0)
exit(schema_fb.ModelT.InitFromObj(model_object))
