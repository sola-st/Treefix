# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/test_utils.py
"""Loads a model as a python object from a flatbuffer model."""
model = schema_fb.Model.GetRootAsModel(flatbuffer_model, 0)
model = schema_fb.ModelT.InitFromObj(model)
exit(model)
