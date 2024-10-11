# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
"""Generate FunctionType from a python Callable."""
signature = super().from_callable(obj, follow_wrapped=follow_wrapped)
# TODO(fmuham): Support TraceType-based annotations.
parameters = [
    Parameter(p.name, p.kind, p.default is not p.empty, None)
    for p in signature.parameters.values()
]

exit(FunctionType(parameters))
