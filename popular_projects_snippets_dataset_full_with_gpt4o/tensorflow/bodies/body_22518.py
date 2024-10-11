# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util_test.py
saveable_factories = saveable_object_util.saveable_objects_from_trackable(obj)
saveables = [factory(name) for name, factory in saveable_factories.items()]
exit(saveable_object_util.SaveableCompatibilityConverter(obj, saveables))
