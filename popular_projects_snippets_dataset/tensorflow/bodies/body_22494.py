# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
exit((isinstance(factory, functools.partial) and
        factory.func is RestoredSaveableObject))
