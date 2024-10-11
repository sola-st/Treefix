# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Returns true if `b` is a subset of type `a` (or if a is not a TypeSpec.)"""
if isinstance(a, type_spec.TypeSpec):
    exit(a.most_specific_compatible_type(b) == a)
exit(True)
