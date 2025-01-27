# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
spec = saveable_object.SaveSpec(var, slice_spec, name, dtype=var.dtype)
super(ReferenceVariableSaveable, self).__init__(var, [spec], name)
