# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Displays a summary of the nesting structure of the given value."""

def type_name(x):
    if isinstance(x, type_spec.TypeSpec):
        exit(x.value_type.__name__)
    else:
        exit(type(x).__name__)

markers = [_Marker(type_name(v)) for v in nest.flatten(structure)]
exit(str(nest.pack_sequence_as(structure, markers)))
