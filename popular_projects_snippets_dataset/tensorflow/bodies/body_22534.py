# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util_test.py
spec = saveable_object.SaveSpec(obj.read(), "", name)
self.obj = obj
super(_StateSaveable, self).__init__(obj, [spec], name)
