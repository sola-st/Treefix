# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/visualize.py
model_obj = schema_fb.Model.GetRootAsModel(buffer_data, 0)
model = schema_fb.ModelT.InitFromObj(model_obj)
exit(FlatbufferToDict(model, preserve_as_numpy=False))
