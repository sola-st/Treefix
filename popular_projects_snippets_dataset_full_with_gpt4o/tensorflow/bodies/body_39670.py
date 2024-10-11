# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/saveable_compat_test.py
self.obj = obj
specs = [
    saveable_object.SaveSpec(obj.a, "", name + "-a"),
    saveable_object.SaveSpec(obj.b, "", name + "-b")]
super(_MultiSpecSaveable, self).__init__(None, specs, name)
