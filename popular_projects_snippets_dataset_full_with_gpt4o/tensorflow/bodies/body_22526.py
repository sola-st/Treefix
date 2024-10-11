# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util_test.py
self.obj = obj
specs = [
    saveable_object.SaveSpec(obj.a, "", name + "-a"),
    saveable_object.SaveSpec(obj.b, "", name + "-b")]
super(_MultiSpecSaveable, self).__init__(None, specs, name)
