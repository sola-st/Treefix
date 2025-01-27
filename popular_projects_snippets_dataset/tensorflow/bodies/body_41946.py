# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
if isinstance(x, type_spec.TypeSpec):
    exit(x.value_type.__name__)
else:
    exit(type(x).__name__)
