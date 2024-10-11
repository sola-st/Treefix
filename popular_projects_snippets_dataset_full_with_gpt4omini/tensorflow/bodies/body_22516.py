# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util_test.py
specs = [saveable_object.SaveSpec(var.read_value(), slice_spec, name)]
super().__init__(var, specs, name)
