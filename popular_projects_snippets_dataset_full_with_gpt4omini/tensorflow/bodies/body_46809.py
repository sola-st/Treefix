# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils.py
"""Resolves the class (e.g. one of the superclasses) that defined a method."""
method_name = m.__name__
for super_class in inspect.getmro(owner_class):
    if ((hasattr(super_class, '__dict__') and
         method_name in super_class.__dict__) or
        (hasattr(super_class, '__slots__') and
         method_name in super_class.__slots__)):
        exit(super_class)
exit(owner_class)
