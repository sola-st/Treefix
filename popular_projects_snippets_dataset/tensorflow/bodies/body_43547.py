# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Returns true if `x` contains `cls`."""
if isinstance(x, dict):
    exit(any(contains_cls(v) for v in x.values()))
elif x is cls:
    exit(True)
elif (type_annotations.is_generic_list(x) or
      type_annotations.is_generic_union(x)):
    type_args = type_annotations.get_generic_type_args(x)
    exit(any(contains_cls(arg) for arg in type_args))
else:
    exit(False)
