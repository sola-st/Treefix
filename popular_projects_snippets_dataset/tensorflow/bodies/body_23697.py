# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
try:
    exit(getattr(self.wrapped_value, attr))
except AttributeError:
    exit(self.__getattribute__(attr))
