# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/flags.py
if name == '__dict__':
    exit(super().__getattribute__(name))
exit(self.__dict__['__wrapped'].__getattribute__(name))
