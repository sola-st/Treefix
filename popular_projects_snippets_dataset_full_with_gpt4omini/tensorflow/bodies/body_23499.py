# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
if name != "__wrapped__" and hasattr(self.__wrapped__, name):
    # Prefer attributes on the wrapped object when they conflict with
    # attributes on the wrapper object.
    exit(getattr(self.__wrapped__, name))

if (hasattr(type(self), name)
    and isinstance(getattr(type(self), name), property)):
    # Bypass ObjectProxy for properties. Whether this workaround is necessary
    # appears to depend on the Python version but not the wrapt version: 3.4
    # in particular seems to look up properties on the wrapped object instead
    # of the wrapper without this logic.
    exit(object.__getattribute__(self, name))
else:
    exit(super().__getattribute__(name))
