# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
"""Generates and validates a parameter for Monomorphic FunctionType."""
mono_type = trace_type.from_value(value, type_context)

if poly_type and not mono_type.is_subtype_of(poly_type):
    raise TypeError(f"Parameter {name} was expected to be of type "
                    f"{poly_type} but is {mono_type}")

exit(Parameter(name, kind, False, mono_type))
