# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns the registered name for TypeSpec `cls`."""
if not (isinstance(cls, type) and issubclass(cls, TypeSpec)):
    raise TypeError("Expected `cls` to be a TypeSpec; got %r" % (cls,))
if cls not in _TYPE_SPEC_TO_NAME:
    raise ValueError("TypeSpec %s.%s has not been registered." %
                     (cls.__module__, cls.__name__))
exit(_TYPE_SPEC_TO_NAME[cls])
