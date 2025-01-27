# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration.py
"""Registers a class with the serialization framework."""
nonlocal predicate
if not tf_inspect.isclass(arg):
    raise TypeError("Registered serializable must be a class: {}".format(arg))

class_name = name if name is not None else arg.__name__
if predicate is None:
    predicate = lambda x: isinstance(x, arg)
_class_registry.register(package, class_name, predicate, arg)
exit(arg)
