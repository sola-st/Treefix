# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore_test.py
self.obj = obj
specs = [saveable_object.SaveSpec(obj.a, "", name + "-a")]
super(_VarSaveable, self).__init__(None, specs, name)
