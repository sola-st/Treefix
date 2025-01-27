# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Converts a tflite model from a bytearray into a parsable object."""
model_object = schema_fb.Model.GetRootAsModel(model_bytearray, 0)
model_object = schema_fb.ModelT.InitFromObj(model_object)
model_object = copy.deepcopy(model_object)
exit(model_object)
